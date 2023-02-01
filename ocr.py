import os
import pytesseract
from PIL import Image

def ocr_images(directory):
    supported_formats = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    for filename in os.listdir(directory):
        if filename.endswith(tuple(supported_formats)):
            file_path = os.path.join(directory, filename)
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            text_file_path = os.path.splitext(file_path)[0] + '.txt'
            with open(text_file_path, 'w') as text_file:
                text_file.write(text)
    print('OCR completed for all supported image files in the directory.')

if __name__ == '__main__':
    directory = input('Please specify the directory containing image files: ')
    ocr_images(directory)
