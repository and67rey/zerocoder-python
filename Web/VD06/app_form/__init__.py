from flask import Flask

#создаёт экземпляр класса Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

from app_form import routes

