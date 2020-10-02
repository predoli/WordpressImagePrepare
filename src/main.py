import argparse
from metaCleaner import MetaCleaner
from imageResizer import ImageResizer
from imageRenamer import ImageRenamer


def main():
    parser = argparse.ArgumentParser(description='Rename and Resize Images')
    parser.add_argument('-c', dest='conf_file', type=str, help='configuration file in json format', default='src/conf.json')
    parser.add_argument('files', metavar='files', type=str, nargs='+', help='image files')
    args = parser.parse_args()
    files = args.files
    conf_file = args.conf_file

    for file in files:
        print(file)
        m = ImageRenamer(file)
        MetaCleaner(conf_file, m.filename)
        ImageResizer(conf_file, m.filename)

if __name__ == "__main__":
    main()