#!/usr/bin/env python
""" Package install script. """

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


f = open(os.path.join(os.path.dirname(__file__), "README.md"))
readme = f.read()
f.close()

setup(
    name="pdfjinjax",
    version="1.2.1",
    author="Edgar Felix",
    author_email="eaafelix@gmail.com",
    url="http://github.com/edgaraafelix/pdfjinjax/",
    description='Use jinja templates to fill and sign PDF forms, based on rammie/pdfjinja with a few enhancements.',
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=["pdfjinjax"],
    entry_points={"console_scripts": ["pdfjinjax = pdfjinja:main"]},
    install_requires=[
        "fdfgen>=0.13.0",
        "jinja2>=2.8",
        "pdfminer.six==20160202",
        "Pillow>=3.2.0",
        "PyPDF2>=1.25.1",
        "reportlab>=3.3.0"
    ])
