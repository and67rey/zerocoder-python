from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://zenquotes.io/api/random"

def get_random_quote():
    """Получает случайную цитату из ZenQuotes API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            return {"text": data[0]["q"], "author": data[0]["a"]}
        else:
            return {"text": "Не удалось получить цитату.", "author": "Ошибка"}
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении цитаты: {e}")
        return {"text": "Ошибка соединения с API.", "author": "Сервер"}

@app.route("/")
def index():
    """Главная страница с цитатой."""
    quote = get_random_quote()
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)

