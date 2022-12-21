from PIL import Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\\Users\\aniln\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
image = cv2.imread('F:/VS_CODE/Avinashi_task/ATM_Slip/images/1.jpg')
text = pytesseract.image_to_string(image)
print(text)