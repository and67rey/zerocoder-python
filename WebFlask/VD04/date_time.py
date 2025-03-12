from flask import Flask
from datetime import date, datetime

app = Flask(__name__)

@app.route("/")
def date_and_time():
    return '''
    <html>
        <head>
            <meta http-equiv="refresh" content="1">
        </head>
        <body>
            <p>Текущая дата: {}</p>
            <p>Текущее время: {}</p>
        </body>
    </html>
    '''.format(date.today(), datetime.now().time().replace(microsecond=0))

if __name__ == "__main__":
    app.run()