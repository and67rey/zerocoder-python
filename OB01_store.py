class Store:
    def __init__(self, name, address):
        """
        Конструктор для инициализации магазина.
        :param name: Название магазина
        :param address: Адрес магазина
        """
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """
        Добавляет товар в ассортимент магазина.
        :param item_name: Название товара
        :param price: Цена товара
        """
        self.items[item_name] = price

    def remove_item(self, item_name):
        """
        Удаляет товар из ассортимента магазина.
        :param item_name: Название товара
        """
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """
        Возвращает цену товара по его названию.
        :param item_name: Название товара
        :return: Цена товара или None, если товара нет в ассортименте
        """
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """
        Обновляет цену товара.
        :param item_name: Название товара
        :param new_price: Новая цена товара
        """
        if item_name in self.items:
            self.items[item_name] = new_price

    def store_info(self):
        """Выводит информацию о магазине"""
        print(f'Информация о магазине: {self.name}')
        print(f'Адрес: {self.address}')
        print('Ассортимент:')
        for key in self.items:
            print(f'\t{key} по цене {self.items[key]}')
        print('\n')


# Создание магазинов
store1 = Store("Fresh Market", "123 Main St")
store2 = Store("Tech World", "456 Tech Ave")
store3 = Store("Book Haven", "789 Book Blvd")

# Добавление товаров
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store2.add_item("laptop", 1200)
store2.add_item("keyboard", 100)
store3.add_item("book", 15)
store3.add_item("magazine", 5)

# Вывод информации о магазинах
store1.store_info()
store2.store_info()
store3.store_info()

# Тестирование методов для store1
# Информация о магазине
store1.store_info()
# Добавление товара
item_name = "walnuts"
store1.add_item(item_name, 1.5)
print(f"Цена {item_name}: {store1.get_price(item_name)}")
# Обновление цены на товар
item_name = "apples"
store1.update_price(item_name, 0.6)
# Проверяем обновленную цену
print(f"Новая цена {item_name}: {store1.get_price(item_name)}")
# Удаление товара
item_name = "bananas"
store1.remove_item(item_name)
print(f"Цены после удаления {item_name}: {store1.items}")  # Проверяем изменения
# Запрос цены на отсутствующий товар
item_name = "oranges"
print(f"Цена товара {item_name}: {store1.get_price(item_name)}")  # Тест товара, которого нет
print('\n')
# Информация о магазине
store1.store_info()
