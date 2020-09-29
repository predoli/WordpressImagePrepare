from src.metaCleaner import MetaCleaner
from src.imageResizer import ImageResizer
from src.imageRenamer import ImageRenamer

local_filename = '../..'
m = ImageRenamer(local_filename)
[MetaCleaner('conf.json', f) for f in m.filename]
[ImageResizer('conf.json', f) for f in m.filename]
