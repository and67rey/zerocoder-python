from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

def find_topic(driver):
    # Находим окно поиска
    search_box = driver.find_element(By.ID, "searchInput")
    user_search = input('Введите тему для поиска публикаций в Википедии: ')
    search_box.send_keys(user_search)
    search_box.send_keys(Keys.RETURN)
    try:
        header = driver.find_element(By.CSS_SELECTOR, "h1")  # Проверяем заголовок страницы
        if header.text == "Результаты поиска":
            print("Вы находитесь на странице результатов поиска")
            # Переход на одну из страниц по выбранной теме
            enter_point = driver.find_element(By.CLASS_NAME, 'searchmatch')
            enter_point.click()
            article_name = browser.find_element(By.CLASS_NAME, 'mw-page-title-main').get_attribute('textContent')
            print(f'Вы перешли на страницу: {article_name}\n')
        else:
            article_name = browser.find_element(By.CLASS_NAME, 'mw-page-title-main').get_attribute('textContent')
            print(f'Вы перешли на страницу: {article_name}\n')
    except NoSuchElementException:
        article_name = browser.find_element(By.CLASS_NAME, 'mw-page-title-main').get_attribute('textContent')
        print(f'Вы перешли на страницу: {article_name}\n')
    time.sleep(3)

# Функция для поиска всех ссылок на странице, сохраняет в словарь
def find_all_links(driver):
    # Найти все ссылки на странице
    elements = driver.find_elements(By.TAG_NAME, 'a')
    # Сохранить ссылки в словарь
    links_dict = {}
    for element in elements:
        link_text = element.text
        link_href = element.get_attribute('href')
        # Проверка на пустые значения
        if link_text and link_href:
            links_dict[link_text] = link_href
    print(f'Всего ссылок на странице: {len(links_dict)}')
    return links_dict

# Функция для поиска всех основных статей на странице, сохраняет в список
def find_all_hatnotes(driver):
    hatnotes = []
    for element in driver.find_elements(By.TAG_NAME, "div"):
        # Чтобы искать атрибут класса
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable ts-main":
            hatnotes.append(element)
    print(f'Всего основных статей на странице: {len(hatnotes)}')
    return hatnotes

# Выбор браузера
browser_choice = input('Выберите браузер: 1 - Chrome, 2 - FireFox\nВаш выбор: ')
match browser_choice:
    case '1':
        browser = webdriver.Chrome()
    case '2':
        browser = webdriver.Firefox()
    case '_':
        browser = webdriver.Chrome()

# Начальная страница для входа
start_point = "https://ru.wikipedia.org/wiki/Заглавная_страница"
browser.get(start_point)
print('\nВы находитесь на заглавной странице Википедии')

find_topic(browser)

surfing = True
while surfing:
    # Выбор вариантов для продолжения
    choice_a = input('Сделайте выбор:\n'
                     '0 - для завершения\n'
                     '1 - листать параграфы на странице\n'
                     '2 - перейти на одну из связанных страниц\n'
                     '3 - перейти на одну из основных статей для этой страницы\n'
                     '4 - выбрать тему для поиска новой публикации в Википедии\n'
                     'Ваш выбор: ')
    match choice_a:
        case '0':
            surfing = False
            print('Завершение программы')
            time.sleep(3)
        case '1':
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            print(f'Всего параграфов: {len(paragraphs)}')
            for paragraph in paragraphs:
                print(paragraph.text, '\n')
                k = input('Нажмите Enter для вывода следующего параграфа или Q для завершения: ')
                if k.lower() == 'q':
                    break
        case '2':
            all_links = find_all_links(browser)
            if len(all_links) == 0:
                print('На этой странице нет ссылок\n')
                time.sleep(3)
            else:
                # Выбор подходящей ссылки для перехода
                for title, link in all_links.items():
                    transit_link = link
                    print(f"Название ссылки: {title},\n ссылка: {link}\n")
                    link_select = input('Нажмите Enter, чтобы дальше листать ссылки, 1 - для перехода по текущей ссылке: ')
                    if link_select == '1':
                        browser.get(transit_link)
                        article_name = browser.find_element(By.CLASS_NAME, 'mw-page-title-main').get_attribute(
                            'textContent')
                        print(f'Вы перешли на страницу: {article_name}\n')
                        break
        case '3':
            all_hatnotes = find_all_hatnotes(browser)
            if len(all_hatnotes) == 0:
                print('На странице не найдено основных статей\n')
                time.sleep(3)
            else:
                hatnote = random.choice(all_hatnotes)
                # Для получения ссылки нужно найти на сайте тег "a"
                hatnote_link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
                browser.get(hatnote_link)
                article_name = browser.find_element(By.CLASS_NAME, 'mw-page-title-main').get_attribute('textContent')
                print(f'Вы перешли на страницу: {article_name}\n')
                time.sleep(3)
        case '4':
            find_topic(browser)
        case _:
            print('\nОшибочный ввод, повторите ваш выбор')
            time.sleep(3)

browser.quit()
