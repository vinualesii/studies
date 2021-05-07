# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:49:43 2021

@author: Saraiva
"""
# Convert pdf to image file JPEG
from pdf2image import convert_from_path


pages = convert_from_path('teste_recibo.pdf')

for i, image in enumerate(pages):
    fname = "image" + str(i) + ".jpg"
    image.save(fname, "JPEG")