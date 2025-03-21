from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    analysis_result = ""
    sentiment = ""
    score = ""

    if request.method == 'POST':
        if 'analyze' in request.form:
            text = request.form.get('text_input', '')
            sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
            result = sentiment_pipeline(text)[0]  # Получаем предсказание

            label = result['label']
            score = result['score'] if 'score' in result else 0.5  # Уверенность модели

            # Модель RoBERTa может выдавать 'LABEL_0', 'LABEL_1', 'LABEL_2'
            label_mapping = {
                "LABEL_0": "Негативная",
                "LABEL_1": "Нейтральная",
                "LABEL_2": "Позитивная"
            }
            sentiment = label_mapping.get(label, "Нейтральные")  # Определяем категорию

            analysis_result = f"Тональность: {sentiment}, Индекс тональности: {score}"

        elif 'clear' in request.form:
            text = ""
            analysis_result = ""

    return render_template('index.html', text=text, analysis_result=analysis_result, sentiment=sentiment, score=score)

if __name__ == '__main__':
    app.run(debug=True)