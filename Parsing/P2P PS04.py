import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


def open_page(web_browser: webdriver, text: str):
    search_box = web_browser.find_element(By.ID, 'searchInput')
    search_box.send_keys(text)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)

def read_by_p(web_browser: webdriver):
    all_paragraphs = web_browser.find_elements(By.TAG_NAME, 'p')
    for paragraph in all_paragraphs:
        if paragraph.text == '':
            continue
        print(paragraph.text)
        if (paragraph.text == 'На этом сайте нет результатов, соответствующих запросу.'
            or paragraph.text == 'Соответствий запросу не найдено.'
        ):
            return
        stop = input('Продолжить - нажмите Enter, остановить вывод - введите "стоп":\n')
        if stop.lower() == 'стоп':
            return

def find_article(web_browser: webdriver):
    a_elements = web_browser.find_elements(By.TAG_NAME, 'a')
    bad_link_classes = ("interlanguage-link-target",
                        "mw-editsection-visualeditor",
                        "wbc-editpage",
                        "external text",
                        "mw-wiki-logo"
    )
    links = []
    link_number = 1
    for elem in a_elements:
        href = elem.get_attribute('href')
        title = elem.get_attribute('title')
        link_class = elem.get_attribute('class')
        if ('Вставить ключевое слово в поле поиска' in title or
            'Возможно, вы имели в виду' in title
        ):
            if len(links) == 0:
                print('На странице не найдены ссылки для связанных статей')
            return None
        if ('Редактировать код раздела «См. также»' in title or
                'Редактировать раздел «Примечания»' in title):
            break
        if (link_class not in bad_link_classes and
            href and
            'wikipedia.org' in href and
            title != '' and
            '(страница отсутствует)' not in title and
            'Википедия:' not in title and
            'Служебная:' not in title and
            'Справка:' not in title and
            'Категория:' not in title and
            'Шаблон:' not in title and
            'Портал:' not in title and
            'Файл:' not in title and
            'Редактировать код раздела ' not in title and
            'Справка о страницах значений' not in title and
            'Править преамбулу' not in title

        ):
            links.append({'link_number': link_number, 'title': title, 'class':link_class, 'href': href})

            print(f'Ссылка № {link_number}, {title} (класс: {link_class}): {href}')
            link_number += 1
    if len(links) == 0:
        print('На странице не найдены ссылки для связанных статей')
        return None
    chosen_number = -1
    while chosen_number == -1:
        try:
            chosen_number = int(input('\nВведите целое число - '
                                      'номер статьи из перечисленных выше для перехода на неё\n'
                                      '(или 0, чтобы вернуться в поиск статей):\n'))
        except:
            print("Номер введён неверно. Попробуйте еще раз. Номера статей перечислены выше. "
                  "Для выхода в поиск по статьям введите 0."
                  )
            continue
        chosen_href = next((d['href'] for d in links if d['link_number'] == chosen_number), None)
        if chosen_href:
            return chosen_href
        elif chosen_number == 0:
            return None
        else:
            chosen_number = -1

browser = webdriver.Firefox()
browser.get('https://ru.wikipedia.org')
print('Добро пожаловать в Википедию!')

while True:
    time.sleep(2)
    article_title = browser.find_element(By.TAG_NAME, 'title').get_attribute('textContent')
    print('Вы находитесь на странице', article_title)
    choose = input('Что желаете делать дальше?\n'
                '1 - открыть интересующую статью\n'
                '2 - читать открытую статью по параграфам\n'
                '3 - выбрать связную статью\n'
                '4 - выйти из программы\n'
                   )
    print('Выбор:', choose)
    if choose.strip() == '1':
        search_word = input('\nВведите слово/фразу для поиска:\n')
        open_page(browser, search_word)
    elif choose.strip() == '2':
        read_by_p(browser)
    elif choose.strip() == '3':
        user_href = find_article(browser)
        if user_href:
            browser.get(user_href)
        else:
            continue
    elif choose.strip() == '4':
        print('До свидания!')
        browser.quit()
        break
    else:
        print('Выбрано неверное значение.')