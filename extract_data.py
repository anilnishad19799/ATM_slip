# import easyocr

# reader = easyocr.Reader(['en']) # need to run only once to load model into memory
# result = reader.readtext('1.jpg')


import easyocr
from easyocr import Reader
import argparse
import cv2

reader = easyocr.Reader(['en']) # need to run only once to load model into memory
result = reader.readtext('1.jpg')
print(result)
# print(easyocr.__version__)