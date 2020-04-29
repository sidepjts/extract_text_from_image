import sys

from PIL import Image
from pytesseract import image_to_string
import pytesseract


def main():
    if sys.platform == 'win32':
        pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

    img = Image.open(sys.argv[1])

    output_text = image_to_string(img)

    print(output_text)

    f = open("output/text_to_file.txt", "a")
    f.write(output_text)
    f.close()


if __name__ == "__main__":
    main()
