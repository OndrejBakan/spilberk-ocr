import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

config = r'--oem 3 --psm 7 outputbase digits -c page_separator='

img = cv2.imread('./img/0-0-4-full.png')

def get_grayscale(image):
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    return cv2.bitwise_not(blackAndWhiteImage)

img_brana = img[42:202, 716:958]
img_tunylek = img[561:721 ,716:958]
img_spz = img[42:202, 1640:1881]

images = [img_brana, img_tunylek, img_spz]

for image in images:
    image = get_grayscale(image)
    text = pytesseract.image_to_string(image, config=config)
    number = int(text)
    
    if number >= 0 and number <= 10000:
        print(number)
    

cv2.imshow('img_brana', img_brana)
cv2.imshow('img_tunylek', img_tunylek)
cv2.imshow('img_spz', img_spz)

cv2.waitKey(0)