from flask import Flask, render_template, request
import requests
from deep_translator import GoogleTranslator

app = Flask(__name__)
NASA_API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "DEMO_KEY"
translator = GoogleTranslator(source='en', target='ru')

def get_apod(date=None):
    """Получает данные APOD с API NASA и переводит заголовок и описание на русский язык."""
    params = {"api_key": API_KEY}
    if date:
        params["date"] = date
    response = requests.get(NASA_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        data["translated_title"] = translator.translate(data.get("title", ""))
        data["translated_explanation"] = translator.translate(data.get("explanation", ""))
        return data
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    date = request.form.get("date")
    apod_data = get_apod(date)
    if apod_data:
        return render_template("index.html",
                               image_url=apod_data.get("url"),
                               title=apod_data.get("title"),
                               translated_title=apod_data.get("translated_title"),
                               explanation=apod_data.get("explanation"),
                               translated_explanation=apod_data.get("translated_explanation"),
                               date=apod_data.get("date", "Сегодня"))
    return "Ошибка при получении данных APOD", 500

if __name__ == "__main__":
    app.run(debug=True)