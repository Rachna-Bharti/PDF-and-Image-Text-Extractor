import easyocr
import pdfplumber
import os

class OCRUtils:
    
    @staticmethod
    def extract_text_from_pdf(pdf_file):
        text = ""
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text

    @staticmethod
    def extract_text_from_image(image_file):
        try:
            # Initialize EasyOCR Reader
            reader = easyocr.Reader(['en'])  # You can add other languages as needed
            # Perform OCR on the image file
            result = reader.readtext(image_file)
            # Extract the text from the result
            text = " ".join([res[1] for res in result])
            return text
        except Exception as e:
            return f"Error extracting text from image: {e}"
