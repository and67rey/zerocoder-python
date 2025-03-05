from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
   api_key = "64cd708d8d9852f8da103ee9e4861700"
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
   weather = None
   if request.method == 'POST':
       city = request.form['city']
       #прописываем переменную, куда будет сохраняться результат и функцию weather с указанием города, который берем из формы
       weather = get_weather(city)
       #передаем информацию о погоде в index.html
   return render_template("index.html", weather=weather)


if __name__ == '__main__':
   app.run(debug=True)