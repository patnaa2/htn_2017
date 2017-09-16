from PIL import Image
import cv2
from pytesseract import *

FILENAME = 'helloworld4.jpg'
negate = False

def main():
    image = cv2.imread(FILENAME)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # write gray file to a file
    if not negate:
        gray_file = 'gray.jpg'
        cv2.imwrite('gray.jpg', gray)

    # try inverted
    if negate:
        negate_g = cv2.bitwise_not(gray)
        inverted_file = 'inverted_gray.jpg'
        cv2.imwrite('inverted_file', negate_g)
        gray_file = inverted_file

    text = pytesseract.image_to_string(Image.open(gray_file))
    print text
    #import pdb ; pdb.set_trace()

if __name__ == '__main__':
    main()
