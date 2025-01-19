from flask import Flask, render_template, request, jsonify
from ocr.ocr_utils import OCRUtils
import os

app = Flask(__name__)

# Path to save uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_text_from_pdf', methods=['POST'])
def extract_text_from_pdf_route():
    if 'pdf_file' not in request.files:
        return "No file part in the request"
    file = request.files['pdf_file']
    if file.filename == '':
        return "No selected file"
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        extracted_text = OCRUtils.extract_text_from_pdf(file_path)
        return render_template('index.html', extracted_text=extracted_text)

@app.route('/extract_text_from_image', methods=['POST'])
def extract_text_from_image_route():
    if 'image_file' not in request.files:
        return "No file part in the request"
    file = request.files['image_file']
    if file.filename == '':
        return "No selected file"
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        extracted_text = OCRUtils.extract_text_from_image(file_path)
        return render_template('index.html', extracted_text=extracted_text)


if __name__ == '__main__':
    app.run(debug=True)
