from flask import Flask, render_template
import requests
from deep_translator import GoogleTranslator

app = Flask(__name__)

API_URL = "https://zenquotes.io/api/random"

def get_random_quote():
    """Получает случайную цитату из ZenQuotes API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            text = data[0]["q"]
            author = data[0]["a"]
            return {"text": text, "author": author}
        else:
            return {"text": "Не удалось получить цитату.", "author": "Ошибка"}
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении цитаты: {e}")
        return {"text": "Ошибка соединения с API.", "author": "Сервер"}

def translate_to_russian(text):
    """Переводит текст на русский язык с помощью Google Translator."""
    try:
        return GoogleTranslator(source='auto', target='ru').translate(text)
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return "Ошибка перевода."

@app.route("/")
def index():
    """Главная страница с цитатами на двух языках."""
    quote = get_random_quote()
    quote["text_ru"] = translate_to_russian(quote["text"])  # Добавляем перевод
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
