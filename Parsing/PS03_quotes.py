from bs4 import BeautifulSoup
import requests
from googletrans import Translator

translator = Translator()

while True:
    page = input('Введите номер страницы или же 1000 для выхода: ')
    if page == '1000':
        break
    elif page == '1':
        url = "http://quotes.toscrape.com/"
    else:
        url = "http://quotes.toscrape.com/" + f'page/{page}/'

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    #Создадим отдельную переменную text, куда будут сохраняться все цитаты
    text = soup.find_all("span", class_="text")
    #Создадим отдельную переменную author, куда будут сохраняться все авторы
    author = soup.find_all("small", class_="author")

    #С помощью функции range(len) определим общее количество цитат
    for i in range(len(text)):
    #Присвоим номер каждой цитате так, чтобы нумерация шла с 1
        print(f"Цитата номер - {i + 1}")
    #Выводим саму цитату, указывая её id
        print(text[i].text)
        ru_text = translator.translate(text[i].text, dest='ru').text
        print(ru_text)
    #Выводим автора цитаты
        ru_author = translator.translate(author[i].text, dest='ru').text
        print(f"Автор цитаты - {author[i].text} / {ru_author}\n")
