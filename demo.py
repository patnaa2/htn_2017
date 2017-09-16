from PIL import Image
import cv2
from pytesseract import *

FILENAME = 'picture.jpg'

def main():
    #image = cv2.imread(FILENAME)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = Image.open(FILENAME).convert('LA')
    img.save('temp.jpg')

    # write gray file to a file
    #cv2.imwrite('gray.jpg', gray)

    # try pytesseract
    text = pytesseract.image_to_string(Image.open('temp.jpg'))
    print(text)

if __name__ == '__main__':
    main()
