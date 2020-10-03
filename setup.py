from setuptools import setup, find_packages

setup(
    name='wordpress-image-prepare',
    version='0.52',
    packages=find_packages(),
    install_requires=['exif>=1.0.1', 'Pillow >= 7.2.0'],
    entry_points={  # Optional
        'console_scripts': ['wordpress-image-prepare=src.main:main'],
    },)