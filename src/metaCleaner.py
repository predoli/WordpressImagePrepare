from exif import Image
import json


class MetaCleaner:
    conf = {}
    filename = ''
    img = None

    def __init__(self, conf_file, filename):
        if filename:
            self.read_conf(conf_file)
            try:
                self.read_image(filename)
                self.replace_exif()
                self.write_image(filename)
            except Exception:
                pass
        else:
            pass

    def read_conf(self, conf_file):
        with open(conf_file) as json_file:
            self.conf = json.load(json_file)

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
#            try:
#                self.img.datetime = str(self.conf['datetime'])
#                self.img.datetime_digitized = self.img.datetime
#                self.img.datetime_original = self.img.datetime
#            except Exception:
#                pass

    def write_image(self, filename):
        with open(filename, 'wb') as new_image_file:
            new_image_file.write(self.img.get_file())