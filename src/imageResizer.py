from PIL import Image
import json


class ImageResizer:
    im = None
    conf = {}

    def __init__(self, conf_file, filename):
        if filename:
            self.read_conf(conf_file)
            self.read_image(filename)
            self.resize_image()
            self.write_image(filename)
        else:
            pass

    def read_image(self, filename):
        self.im = Image.open(filename)

    def read_conf(self, conf_file):
        with open(conf_file) as json_file:
            self.conf = json.load(json_file)

    def resize_image(self):
        conf_size = tuple(self.conf['size'])
        size = self.im.size
        factor = float(size[0])/float(size[1])
        factor_conf = float(conf_size[0]/conf_size[1])
        if 1 <= factor < factor_conf: #landscape height crop
            self.resize_image_height(conf_size)
        elif factor >= 1 and factor >= factor_conf: #landscape width crop
            self.resize_image_width(conf_size)
        elif factor < 1 and factor < 1/factor_conf: #portrait height crop
            self.resize_image_height((conf_size[1], conf_size[0]))
        else: #portrait width crop
            self.resize_image_width((conf_size[1], conf_size[0]))

    def resize_image_width(self, conf_size: tuple):
        scale_factor = float(conf_size[1]) / float(self.im.size[1])
        resize = (int(self.im.size[0] * scale_factor), conf_size[1])
        self.im = self.im.resize(resize)
        self.im = self.im.crop(((resize[0] - conf_size[0])/2, 0, (resize[0] - conf_size[0])/2 + conf_size[0], conf_size[1]))

    def resize_image_height(self, conf_size: tuple):
        scale_factor = float(conf_size[0]) / float(self.im.size[0])
        resize = (conf_size[0], int(self.im.size[1] * scale_factor))
        self.im = self.im.resize(resize)
        self.im = self.im.crop((0, (resize[1] - conf_size[1])/2, conf_size[0], (resize[1] - conf_size[1])/2 + conf_size[1]))

    def write_image(self, filename):
        self.im.save(filename)


