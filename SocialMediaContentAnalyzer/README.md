# Text Extractor

## Overview
Text Extractor is a simple web application that allows users to extract text from PDFs and images. It provides a user-friendly interface with dedicated sections for processing PDF and image files, displaying the extracted text in a separate block.

---

## Features
- **PDF Text Extraction**: Upload a PDF file and extract text from it.
- **Image Text Extraction**: Upload an image file (JPG, PNG, BMP) and extract text using OCR.
- **Clean User Interface**: Separate blocks for PDFs, images, and the extracted text for easy usability.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`)

---

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create required directories if not present:
   ```bash
   mkdir uploads
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open the app in your browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## File Structure
```
/SocialMediaContentAnalyzer
│
├── /assets                     # Stores static assets like images or PDFs for testing
│
├── /ocr                        # Directory to store OCR-related files and scripts
│   ├── ocr_utils.py            # OCR utility functions
│
├── /uploads                   # Directory where users upload files (PDFs, images)
│
├── /static                    # Static files (CSS, JS) for the frontend
│
├── /templates                 # HTML templates
│   ├── index.html              # Main page to upload files and display results
│
├── /app.py                    # Main application file
│
├── /requirements.txt          # Python dependencies
│
├── /README.md                 # Project overview and setup instructions
```

---

## Usage
1. Launch the application and open it in your web browser.
2. **PDF Extraction**:
   - Upload a PDF file in the "Extract Text from PDF" section.
   - Click "Upload PDF."
   - The extracted text will appear in the "Extracted Text" block.
3. **Image Extraction**:
   - Upload an image file in the "Extract Text from Image" section.
   - Click "Upload Image."
   - The extracted text will appear in the "Extracted Text" block.

---

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Flask
- **OCR**: pdfplumber (for PDFs), EasyOCR (for images)

---

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch.
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes.
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your branch.
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---


