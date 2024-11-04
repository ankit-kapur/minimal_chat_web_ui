from flask import Flask, request, render_template, jsonify, send_from_directory, redirect, url_for
from flask_cors import CORS
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
import os

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

received_texts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global received_texts
    if request.method == 'POST':
        text_data = request.form['inputTextArea']
        html_text = markdown.markdown(text_data, extensions=['extra', 'nl2br', 'wikilinks', CodeHiliteExtension(guess_lang=False)])
        received_texts.append(html_text)
    return render_template('chat_ui.html')

@app.route('/messages', methods=['GET'])
def get_messages():
    global received_texts
    return jsonify(received_texts=received_texts[::-1])

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return jsonify({'filename': file.filename})

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8181)