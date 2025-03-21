from flask import Flask, render_template, request, send_file, jsonify
from gtts import gTTS
import os
import time
from werkzeug.utils import secure_filename
import chardet
import fitz


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = 'audio'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

def detect_encoding(filepath):
    with open(filepath, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def extract_text_from_pdf(filepath):
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_text_to_audio():
    text = request.form.get('text', '')
    language = request.form.get('language', 'ru')

    # Обработка загрузки файла
    if 'file' in request.files:
        file = request.files['file']
        if file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            if file.filename.endswith('.pdf'):
                text = extract_text_from_pdf(filepath)
            else:
                encoding = detect_encoding(filepath)
                try:
                    with open(filepath, 'r', encoding=encoding) as f:
                        text = f.read()
                except UnicodeDecodeError:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        text = f.read()  # Пропускаем нераспознанные символы

    if not text.strip():
        return jsonify({'error': 'Пожалуйста, введите текст или загрузите файл'}), 400

    # Генерация аудио
    tts = gTTS(text=text, lang=language)
    audio_filename = f"audio_{int(time.time())}.mp3"
    audio_path = os.path.join(AUDIO_FOLDER, audio_filename)
    tts.save(audio_path)

    print(f"Сохранен файл: {audio_path}, размер: {os.path.getsize(audio_path)} байт")

    return jsonify({'audio_file': audio_filename})  # Возвращаем имя файла


@app.route('/download/<filename>')
def download_audio(filename):
    file_path = os.path.join(AUDIO_FOLDER, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'Файл не найден'}), 404
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

