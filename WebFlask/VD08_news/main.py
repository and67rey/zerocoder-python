from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   news = None
   if request.method == 'GET':
       news = get_news()
   return render_template("index.html", news=news)

def get_news():
   api_key = "cbe8ff8786cc4c19a720ba9e7ce194f5"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', [])

if __name__ == '__main__':
   app.run(debug=True)