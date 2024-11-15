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

# Тестирование методов для store1
print(f"Цены в {store1.name}: {store1.items}")  # Вывод всего ассортимента
store1.update_price("apples", 0.6)  # Обновляем цену яблок
print(f"Новая цена apples: {store1.get_price('apples')}")  # Проверяем обновленную цену
store1.remove_item("bananas")  # Убираем бананы
print(f"Цены после удаления bananas: {store1.items}")  # Проверяем изменения
print(f"Цена товара 'oranges': {store1.get_price('oranges')}")  # Тест товара, которого нет
