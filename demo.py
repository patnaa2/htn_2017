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

    # try inverted
    negate_g = cv2.bitwise_not(gray)
    cv2.imwrite('inverted_gray.jpg', negate_g)

    text = pytesseract.image_to_string(Image.open('inverted_gray.jpg'))
    import pdb ; pdb.set_trace()

if __name__ == '__main__':
    main()
