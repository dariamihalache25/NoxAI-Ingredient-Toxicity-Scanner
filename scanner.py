"""
scanner.py

This helper script is a standalone sandbox for testing the Optical Character Recognition (OCR)
pipeline. It uses Tesseract to extract raw text from product labels and applies string
manipulation and Regular Expressions (Regex) to isolate individual ingredients.
"""
from PIL import Image
import pytesseract
import re

# Set the path for the Tesseract engine (Local Windows environment)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def clear_text_label(messy_text):
    """
    Takes text extracted by OCR and cleans it into a standardized Python list.
    Removes marketing words, normalizes characters, and splits the string into distinct chemicals.
    """
    text = messy_text.upper()

    # Isolate the list by slicing off everything before the colon or the word "INGREDIENTS"
    if ":" in text:
        text = text.split(":")[-1]
    elif "GREDIENT" in text:
        text = text.split("GREDIENT")[-1]

    # Flatten multi-line text into a single line
    text = text.replace('\n', ' ').replace('\r', ' ')
    # Only keep letters, numbers, commas, spaces, and hyphens
    text = re.sub(r'[^A-Z0-9, \-]', '', text)

    # Split the string into a list using either semicolons or commas
    elem_list = re.split(r'[;,]', text)
    clean_list = []
    for element in elem_list:

        # Filter out random letter chunks caused by OCR misreads
        if len(element.strip()) > 3:
            clean_list.append(element.strip())

    return clean_list

# ==========================================
# TEST EXECUTION
# ==========================================
try:
    img = Image.open("test_label.jpg")
    raw_text = pytesseract.image_to_string(img)
    ingredients = clear_text_label(raw_text)

    for i, elem in enumerate(ingredients):
        print(f"{i+1}. {elem}")

except FileNotFoundError:
    print('Error: File was not found.')