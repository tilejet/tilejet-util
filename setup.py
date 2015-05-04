#!/usr/bin/env python

from setuptools import setup

setup(
    name='tilejet-util',
    version='0.0.1',
    install_requires=[],
    author='TileJet Developers',
    author_email='XXX',
    license='MIT License',
    url='https://github.com/tilejet/tilejet-util/',
    keywords='python gis tilejet',
    description='A python utility library containing functions for managing tile services, such as converting between z/x/y to geojson.',
    long_description=open('README.md').read(),
    download_url="https://github.com/tilejet/tilejet-util/zipball/master",
    py_modules=["tilejet-util"],
    classifiers = [
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)