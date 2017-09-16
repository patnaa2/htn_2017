from PIL import Image
import cv2
import pytesseract

FILENAME = 'picture.jpg'

def main():
    image = cv2.imread(FILENAME)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # write gray file to a file
    cv2.imwrite('gray.jpg', gray)

    # try pytesseract
    pytesseract.image_to_string(Image.open('gray.jpg'))

if __name__ == '__main__':
    main()
