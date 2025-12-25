import pytesseract
from PIL import Image
import cv2

# 開啟圖片

#print("請上傳圖片 (建議：白紙黑字，字寫粗一點)")
uploaded = files.upload() #上傳用
image = Image.open(uploaded)

text = pytesseract.image_to_string(image, lang='eng', config='--psm 8') #重點是改語系

print("OCR 辨識結果:")
print("-" * 40)
print(text)