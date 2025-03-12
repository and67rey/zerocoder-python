from flask import render_template, request, redirect, url_for

from app_form import app

data = []

@app.route("/", methods=["GET", "POST"])

def index():
#использует метод POST, так как информация будет отправляться. Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
    #функция request.form извлекает значение из соответствующих полей
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        #создаёт условие для проверки наличия данных в полях
        if name and city:
            data.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
        #использует для обновления страницы и предотвращения повторной отправки формы.
        return redirect(url_for('index'))
        #возвращает отрендеренный шаблон с переданными данными пользователя
    return render_template('form.html', data=data)