"""
Дополненное ДЗ
Добавлена возможность сохранять зоопарк в JSON файл, чтобы его править впоследствии.
Так же добавлены 2 новых поля для Animal - голод и болезнь. Сотрудники отрабатывают свои обязанности
по животным только в случае, если соответствующее им поле True.
Достаточно перед запуском поправить в json поля голода и болезни в true, чтобы ветеринар и управляющий
отработали свои обязанности, после чего поля выставляются ы false и все это сохраняется обратно в JSON файл.

"""




import json


class Animal:
    def __init__(self, name, age,hungry=False,illnes=False):  # Исправлено init на __init__
        self.name = name
        self.age = age
        self.hungry = hungry
        self.illnes = illnes

    def make_sound(self):
        return f"{self.name} молчит "

    def eat(self):
        return f"{self.name} ест"

    def to_dict(self):
        return {"type": self.__class__.__name__, "name": self.name, "age": self.age, "hungry": self.hungry, "illnes": self.illnes}

    @staticmethod
    def from_dict(data):
        if data["type"] == "Bird":
            return Bird(data["name"], data["age"],data["hungry"],data["illnes"])
        elif data["type"] == "Mammal":
            return Mammal(data["name"], data["age"],data["hungry"],data["illnes"])
        elif data["type"] == "Reptile":
            return Reptile(data["name"], data["age"],data["hungry"],data["illnes"])
        return None


# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        return f"{self.name} чирикает!"


# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} рычит!"


# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} шипит."


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Класс Zoo
class Zoo:
    def __init__(self):  # Исправлено init на __init__
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        for animal in self.animals:
            print(f"Зверь: {animal.name}, Возраст: {animal.age}")

    def save_data(self, filename):
        data = {
            "animals": [animal.to_dict() for animal in self.animals],
            "staff": [staff_member.name for staff_member in self.staff]
        }
        with open(filename, 'w',encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print("Данные сохранены в ", filename)

    def load_data(self, filename):
        try:
            with open(filename, 'r',encoding="utf-8") as f:
                data = json.load(f)
                self.animals = [Animal.from_dict(animal) for animal in data["animals"]]
                self.staff = [ZooKeeper(name) if name.startswith("Управляющий") else Veterinarian(name) for name in data["staff"]]
                print("Данные загружены из ", filename)

        except (FileNotFoundError, json.JSONDecodeError):
            print("Данные не найдены, запускаем зоопарк с нуля.")


# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):  # Исправлено init на __init__
        self.name = name

    def feed_animal(self, animal):
        if animal.hungry:
            animal.hungry=False
            return f"{self.name} кормит {animal.name}."




# Класс Veterinarian
class Veterinarian:
    def __init__(self, name):  # Исправлено init на __init__
        self.name = name

    def heal_animal(self, animal):
        if animal.illnes:
            animal.illnes=False
            return f"{self.name} лечит {animal.name}."


# Пример использования
if __name__ == "__main__":  # Исправлено name на __name__
    # Создаем зоопарк
    zoo = Zoo()

    # Пытаемся загрузить данные
    zoo.load_data('zoo_data.json')

    # Если зоопарк пуст, создаем животных
    if not zoo.animals:
        parrot = Bird("Попугай", 2)
        lion = Mammal("Лев", 5)
        snake = Reptile("Змей", 3)

        # Добавляем животных в зоопарк
        zoo.add_animal(parrot)
        zoo.add_animal(lion)
        zoo.add_animal(snake)

    # Показываем животных в зоопарке
    zoo.show_animals()

    # Демонстрируем полиморфизм
    animal_sound(zoo.animals)


    # Если зоопарк пуст, создаем животных
    if not zoo.staff:
        # Создаем сотрудников зоопарка
        keeper = ZooKeeper("Управляющий Василий")
        vet = Veterinarian("Доктор Дуллитл")

        # Добавляем сотрудников в зоопарк
        zoo.add_staff(keeper)
        zoo.add_staff(vet)


    for animal in zoo.animals:
        for employe in zoo.staff:
            try:
                res=employe.feed_animal(animal)
                if res is not None: print(res)
            except Exception as e:
                pass
            try:
                res=employe.heal_animal(animal)
                if res is not None: print(res)
            except Exception as e:
                pass

    # Сохраняем данные о зоопарке
    zoo.save_data('zoo_data.json')