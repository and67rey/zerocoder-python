from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    analysis_result = ""

    if request.method == 'POST':
        if 'analyze' in request.form:
            text = request.form.get('text_input', '')
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            analysis_result = f"Polarity: {polarity}, Subjectivity: {subjectivity}"
        elif 'clear' in request.form:
            text = ""
            analysis_result = ""

    return render_template('index.html', text=text, analysis_result=analysis_result)

if __name__ == '__main__':
    app.run(debug=True)