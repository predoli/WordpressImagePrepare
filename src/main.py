import argparse
import json
from src.metaCleaner import MetaCleaner
from src.imageResizer import ImageResizer
from src.imageRenamer import ImageRenamer


def read_conf(conf_file):
    try:
        with open(conf_file) as json_file:
            return json.load(json_file)
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description='Rename and Resize Images')
    parser.add_argument('-r', dest='image_resize', help='image resize', action='store_true', default=False)
    parser.add_argument('-m', dest='metadata_overwrite', help='metadata overwrite', action='store_true', default=False)
    parser.add_argument('-c', dest='conf_file', type=str, help='configuration file in json format', default=None)
    parser.add_argument('files', metavar='files', type=str, nargs='+', help='image files')
    args = parser.parse_args()
    files = args.files
    image_resize = args.image_resize
    metadata_overwrite = args.metadata_overwrite
    conf = None
    if args.conf_file:
        conf_file = args.conf_file
        conf = read_conf(conf_file)
    if conf is None:
        conf = {
            "size": [2000, 1500],
            "datetime": "2000:00:00 00:00:00",
            "gps_altitude": 8848.0,
            "gps_latitude": [19.0, 16.0, 46.6464],
            "gps_longitude": [166.0, 38.0, 53.0124]
        }

    for file in files:
        print(file)
        m = ImageRenamer(file)
        if metadata_overwrite:
            MetaCleaner(conf, m.filename)
        if image_resize:
            ImageResizer(conf, m.filename)


if __name__ == "__main__":
    main()
