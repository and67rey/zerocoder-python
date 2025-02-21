from flask import Flask
from datetime import date, datetime

app = Flask(__name__)

@app.route("/")

def date_and_time():
    current_date = date.today()
    current_time = datetime.now().time()
    return f'Текущая дата: {current_date}, текущее время: {current_time}'

if __name__ == "__main__":
    app.run()