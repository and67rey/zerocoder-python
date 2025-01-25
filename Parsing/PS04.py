from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

# Функция для поиска всех ссылок на странице, сохраняет в словарь
def find_all_links(url, driver):
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
def find_all_hatnotes(url, driver):
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        # Чтобы искать атрибут класса
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable ts-main":
            hatnotes.append(element)
    print(f'Всего основных статей на странице: {len(hatnotes)}')
    return hatnotes


browser = webdriver.Chrome()

# Начальная страница для входа
start_point = "https://ru.wikipedia.org/wiki/Заглавная_страница"
browser.get(start_point)

#Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")

user_search = input('Ввести тему для поиска публикаций в Википедии: ')
search_box.send_keys(user_search)
search_box.send_keys(Keys.RETURN)

time.sleep(3)
# Переход на одну из страниц по выбранной теме
enter_point = browser.find_element(By.LINK_TEXT, user_search)
enter_point.click()

# Выбор вариантов для продолжения
case = input('Сделайте выбор:\n 0 - для завершения;\n 1 - листать параграфы на странице;\n 2 - перейти на одну из связанных страниц; \nВаш выбор: ')

if case == '0':
    print('Завершение программы')
    time.sleep(3)
elif case == '1':
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    print(f'Всего параграфов: {len(paragraphs)}')
    for paragraph in paragraphs:
        print(paragraph.text, '\n')
        k = input('Нажмите Enter для вывода следующего параграфа или Q для завершения: ')
        if k.lower() == 'q':
            break
elif case == '2':
    all_links = find_all_links(enter_point, browser)
    random_item = random.choice(list(all_links.items()))
    title = random_item[0]
    link = random_item[1]
    print(f"Случайная ссылка для перехода: {title}\n ссылка: {link}")
    browser.get(link)
    case_2 = input('Сделайте выбор:\n 0 - для завершения;\n 1 - листать параграфы на странице;\n 2 - перейти на одну из основных статей; \nВаш выбор: ')
    if case_2 == '0':
        print('Завершение программы')
        time.sleep(3)
    elif case_2 == '1':
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        print(f'Всего параграфов: {len(paragraphs)}')
        for paragraph in paragraphs:
            print(paragraph.text, '\n')
            k = input('Нажмите Enter для вывода следующего параграфа или Q для завершения: ')
            if k.lower() == 'q':
                break
    elif case_2 == '2':
        all_hatnotes = find_all_hatnotes(link, browser)
        hatnote = random.choice(all_hatnotes)
        # Для получения ссылки нужно найти на сайте тег "a"
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        time.sleep(10)
    else:
        print('Завершение программы')
        time.sleep(3)
else:
    print('Завершение программы')
    time.sleep(3)

browser.quit()






