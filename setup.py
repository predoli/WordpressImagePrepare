from setuptools import setup, find_packages

setup(
    name='wordpress-image-prepare',
    version='0.5',
    package_dir={'':'src'},
    py_modules=['main', 'imageRenamer', 'imageResizer', 'metaCleaner'],
    install_requires=['exif>=1.0.1', 'Pillow >= 7.2.0'],
    entry_points={  # Optional
        'console_scripts': ['wordpress-image-prepare=WordpressImagePrepare.main:main'],
    },)