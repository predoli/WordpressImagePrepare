import argparse

from src.metaCleaner import MetaCleaner
from src.imageResizer import ImageResizer
from src.imageRenamer import ImageRenamer

parser = argparse.ArgumentParser(description='Rename and Resize Images')

parser.add_argument('conf_file', metavar='conf_file', type=str,
                    help='configuration file in json format')

parser.add_argument('files', metavar='files', type=str, nargs='+',
                    help='image files')

args = parser.parse_args()
files = args.files

conf_file = args.conf_file

for file in files:
    m = ImageRenamer(file)
    MetaCleaner(conf_file, m.filename)
    ImageResizer(conf_file, m.filename)

