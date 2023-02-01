# OCR-Script
Use:
Ask the user to supply a directory and all supported image files in the directory are OCR'd and there is a .txt file created contains the same name as the image filename.

Instructions:
Install Tesseract by following the instructions on their official website https://github.com/UB-Mannheim/tesseract/wiki
Add .exe location to PATH (for me it was C:\Program Files\Tesseract-OCR )
pip install pytesseract



Line by line code explanation:

This program is a simple Optical Character Recognition (OCR) script in Python. It uses the libraries os, pytesseract and PIL (Python Imaging Library).

The first line import os is for using the functionality provided by the os module in Python to interact with the operating system.

The second line import pytesseract is for importing the pytesseract library which is a wrapper for the Tesseract OCR engine. This library helps in processing images and recognizing text in them.

The third line from PIL import Image is for importing the Image class from the PIL library. This class will be used to open image files.

The next part is the ocr_images function. This function takes a directory path as an argument and performs OCR on all supported image files present in that directory.

The first line supported_formats = ['.png', '.jpg', '.jpeg', '.bmp', '.gif'] is a list of file extensions of image formats supported by the program.

The next line for filename in os.listdir(directory): loops through all files in the given directory using the os.listdir function.

The next line if filename.endswith(tuple(supported_formats)): checks if the current file is a supported image format based on its file extension.

The next line file_path = os.path.join(directory, filename) is used to create the full file path of the current image file using the os.path.join function.

The next line image = Image.open(file_path) opens the current image file using the Image.open method.

The next line text = pytesseract.image_to_string(image) uses the pytesseract.image_to_string function to recognize text in the current image.

The next line text_file_path = os.path.splitext(file_path)[0] + '.txt' creates the full file path of the text file to be created. The text file name is derived from the image file name by removing its extension and adding '.txt' to it.

The next line with open(text_file_path, 'w') as text_file: opens the text file for writing and the following line text_file.write(text) writes the recognized text to the text file.

The final line print('OCR completed for all supported image files in the directory.') prints a message indicating that OCR has been completed for all supported image files in the directory.

The final part of the code if __name__ == '__main__': is a special check in Python which tells the interpreter that this code should only be executed if it is run as the main program and not imported as a module.

The line directory = input('Please specify the directory containing image files: ') prompts the user to input the directory path containing the image files.

The line ocr_images(directory) calls the ocr_images function and passes the directory path as an argument.

