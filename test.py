import cv2
import pytesseract
import yagmail

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

config = r'--oem 3 --psm 7 outputbase digits -c page_separator='

img = cv2.imread('./img/947-1124-92.png')

def get_grayscale(image):
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 158, 255, cv2.THRESH_BINARY)
    return cv2.bitwise_not(blackAndWhiteImage)

img_brana = img[36:36+105, 485:485+158]
img_tunylek = img[384:384+105, 483:483+158]
img_spz = img[32:32+105, 1089:1089+158]

images = [
    img_brana,
    img_tunylek,
    img_spz
]

res = []
for image in images:
    image = get_grayscale(image)
    text = pytesseract.image_to_string(image, config=config)
    number = int(text)
    
    if number >= 0 and number <= 10000:
        res.append(number)

body = [
    'Brána: {}'.format(res[0]),
    'Tunýlek: {}'.format(res[1]),
    'SPZ: {}'.format(res[2]),
]

#yag = yagmail.SMTP('ondrej@bakan.cz')
#yag.send('velin@spilberk.cz', 'Průchod', body)

cv2.imshow('img_brana', img_brana)
cv2.imshow('img_tunylek', img_tunylek)
cv2.imshow('img_spz', img_spz)

cv2.waitKey(0)