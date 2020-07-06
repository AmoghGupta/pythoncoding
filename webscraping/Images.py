#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:23:19 2020

@author: agupta
"""

from PIL import Image

#referring to image
mac = Image.open("example.png")

#showing image
#mac.show()


print(mac.filename)

print(mac.format_description)

mac.crop((10,10,10,10))

mac.save("cropped.png")


