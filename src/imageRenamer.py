import os
from pathlib import Path
from PIL import Image, UnidentifiedImageError
import re
import sys


class ImageRenamer:
    def __init__(self, filename):
        self.filename = None
        if filename and os.path.isfile(filename):
            try:
                im = Image.open(filename)
                im.verify()
                self.filename = self.change_file_name(os.path.join(os.getcwd(), filename))
            except Exception:
                pass

    def change_file_name(self, file_path):
        parent_path = os.path.dirname(file_path)
        new_file_name_prefix = Path(parent_path).resolve().stem
        if not re.match(r""+new_file_name_prefix+"_\d*.jpg$", os.path.basename(file_path)):
            file_list = [f for f in os.listdir(parent_path) if re.match(r""+new_file_name_prefix+".*.jpg$", f)]
            if file_list:
                n = max([int(f.split('_')[-1].split('.')[0]) for f in file_list])
            else:
                n = 0
            filename, file_extension = os.path.splitext(file_path)
            new_file_path = os.path.join(parent_path, new_file_name_prefix + "_" + str(n+1) + file_extension)
            os.rename(r""+file_path, r""+new_file_path)
            return new_file_path
        else:
            return file_path





