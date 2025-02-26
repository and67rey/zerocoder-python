from flask import Flask

#создаёт экземпляр класса Flask (переменную app_blog)
app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

from app_blog import routes

