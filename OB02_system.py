class User:
    """
    Класс, представляющий обычного сотрудника.
    Содержит ID, имя и уровень доступа.
    """
    def __init__(self, user_id: int, name: str):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    # Методы для получения данных
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Метод для получения текстового описания пользователя
    def describe(self):
        return f"User[ID: {self.__user_id}, Name: {self.__name}, Access: {self.__access_level}]"


class Admin(User):
    """
    Класс администратора, наследует функционал класса User.
    Добавляет возможность управлять пользователями.
    """
    def __init__(self, user_id: int, name: str, admin_level: int):
        super().__init__(user_id, name)
        self.__admin_level = admin_level

    # Метод для получения уровня администратора
    def get_admin_level(self):
        return self.__admin_level

    # Метод для добавления пользователя
    def add_user(self, user_list: list, user: User):
        if not isinstance(user, User):
            raise TypeError("Объект должен быть экземпляром класса User.")
        user_list.append(user)
        print(f"Пользователь {user.get_name()} успешно добавлен.")

    # Метод для удаления пользователя
    def remove_user(self, user_list: list, user_id: int):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} (ID: {user_id}) успешно удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    # Метод для получения текстового описания администратора
    def describe(self):
        return f"Admin[ID: {self.get_user_id()}, Name: {self.get_name()}, Access: admin, Level: {self.__admin_level}]"


# Пример использования

# Создаем список пользователей
user_list = []

# Создаем администратора
admin = Admin(user_id=1, name="Alice", admin_level=5)

# Добавляем пользователей
user1 = User(user_id=2, name="Bob")
user2 = User(user_id=3, name="Charlie")
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)

# Вывод списка пользователей
print("\nСписок пользователей:")
for user in user_list:
    print(user.describe())

# Удаляем пользователя
admin.remove_user(user_list, user_id=2)

# Вывод списка пользователей после удаления
print("\nСписок пользователей после удаления:")
for user in user_list:
    print(user.describe())

    # Печатаем данные администратора
    print("\nДанные администратора:")
    print(admin.describe())
