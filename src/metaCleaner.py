from exif import Image
import json


class MetaCleaner:
    conf = {}
    filename = ''
    img = None

    def __init__(self, conf, filename):
        if filename:
            self.conf = conf
            try:
                self.read_image(filename)
                self.replace_exif()
                self.write_image(filename)
            except Exception:
                pass
        else:
            pass

    def read_image(self, filename):
        with open(filename, 'rb') as image_file:
            self.img = Image(image_file)

    def replace_exif(self):
        if self.img.has_exif:
            self.img.software = 'OLIWARE'
            self.img.gps_altidue = float(self.conf['gps_altitude'])
            self.img.gps_latitude = tuple(self.conf['gps_latitude'])
            self.img.gps_longitude = tuple(self.conf['gps_longitude'])
            self.img.gps_datestamp = str(self.conf['datetime']).split(' ')[0]
            self.img.gps_timestamp = tuple([float(x) for x in (str(self.conf['datetime']).split(' ')[1].split(':'))])

    def write_image(self, filename):
        with open(filename, 'wb') as new_image_file:
            new_image_file.write(self.img.get_file())