#!/usr/bin/env python

import os

from distutils.core import setup
setup(
    name = "pcd8544",
    version = "0.0.1",
    author = "Richard Hull",
    author_email = "richard.hull@destructuring-bind.org",
    description = ("A small library to drive the PCD8544 LCD using WiringPi software bit-banding"),
    license = "BSD",
    keywords = "raspberry pi rpi lcd nokia 5110 pcd8544",
    url = "https://github.com/rm-hull/pcd8544",
    packages=['pcd8544'],
    package_dir={'pcd8544': 'src'}
)

print "--- Installing LCD service daemon ---"
os.chdir("scripts")
os.system("./installLCDd.sh")
