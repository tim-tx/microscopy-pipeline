from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "microscopy-pipeline",
    version = "0.0.1",
    author = "Timothy Jones",
    author_email = "tjones01@gmail.com",
    description = "A pipeline to combine image processing and cytometry-style calibration",
    license = "GPLv3 with linking exception",
    keywords = "image-processing microscopy cytometry",
    url = "https://github.com/tim-tx/microscopy-pipeline",
    packages = find_packages(),
    install_requires = ["microtaspy",
                        "cytoflow"],
    long_description = read('README.org'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ]
)
