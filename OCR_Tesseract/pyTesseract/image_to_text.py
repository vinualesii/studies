# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:08:33 2021

@author: Saraiva
"""
import cv2
import pytesseract
from pytesseract import Output


image = cv2.imread('image0.jpg')

custom_config = r'--oem 3 --psm 6'

print(pytesseract.image_to_string(image, config=custom_config))