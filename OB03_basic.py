# Базовый класс Animal
class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе.")

    def eat(self):
        print(f"{self.name} ест пищу.")

    def sleep(self):
        print(f"{self.name} спит.")

    def move(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе.")

# Подкласс Bird
class Bird(Animal):
    def __init__(self, name: str, age: int, wing_span: float, sound: str):
        super().__init__(name, age)
        self.wing_span = wing_span
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издает звук - {self.sound}.")

    def move(self):
        print(f"{self.name} летает с размахом крыльев {self.wing_span} метров.")

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name: str, age: int, fur_color: str, sound: str):
        super().__init__(name, age)
        self.fur_color = fur_color
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издает звук - {self.sound}.")

    def move(self):
        print(f"{self.name} бегает.")

# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name: str, age: int, length: float, sound: str):
        super().__init__(name, age)
        self.length = length
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издает звук - {self.sound}.")

    def move(self):
        print(f"{self.name} ползает.")

# Функция демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Базовый класс Employee
class Employee:
    def __init__(self, name: str, experience: int):
        self.name = name
        self.experience = experience

# Класс ZooKeeper
class ZooKeeper(Employee):
    def __init__(self, name: str, experience: int):
        super().__init__(name, experience)
        self.specialty = 'Смотритель зоопарка'

    def feed_animal(self, animal: Animal):
        print(f"{self.name} кормит животное - {animal.name}.")

    def show_employees(self):
        print(f"  - Имя: {self.name}, Опыт: {self.experience} лет, Специальность: {self.specialty}")

# Класс Veterinarian
class Veterinarian(Employee):
    def __init__(self, name: str, experience: int):
        super().__init__(name, experience)
        self.specialty = 'Ветеринар'

    def heal_animal(self, animal: Animal):
        print(f"{self.name} лечит животное - {animal.name}.")

    def show_employees(self):
        print(f"  - Имя: {self.name}, Опыт: {self.experience} лет, Специальность: {self.specialty}")

# Класс Zoo
class Zoo:
    def __init__(self, name: str):
        self.name = name
        self.animals = []  # Список животных
        self.employees = []  # Список сотрудников

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен в зоопарк.")

    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"  - Имя: {animal.name}, Возраст: {animal.age}")

    def show_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            employee.show_employees()
            # print(f"  - Имя: {employee.name}, Опыт: {employee.experience} лет")

# Пример использования

# Создание животных
parrot = Bird(name="Попугай", age=3, wing_span=0.5, sound = 'Гоша хороший')
eagle = Bird(name="Орел", age=5, wing_span=2, sound = 'кииииии-иа')
lion = Mammal(name="Лев", age=4, fur_color="золотистый", sound = 'ррррр')
bear = Mammal(name="Медведь", age=7, fur_color="бурый", sound = 'ррррааау')
snake = Reptile(name="Змея", age=2, length=2.1, sound = 'шшшшшш')
crocodile = Reptile(name="Крокодил", age=6, length=2.5, sound = 'грруууу')

# Создание сотрудников
keeper1 = ZooKeeper(name="Иван Иванов", experience=7)
vet1 = Veterinarian(name="Анна Смирнова", experience=5)
keeper2 = ZooKeeper(name="Федор Кузнецов", experience=4)
vet2 = Veterinarian(name="Ольга Петрова", experience=6)

# Создание зоопарка
zoo = Zoo(name="Городской зоопарк")

# Добавление животных и сотрудников в зоопарк
zoo.add_animal(parrot)
zoo.add_animal(eagle)
zoo.add_animal(lion)
zoo.add_animal(bear)
zoo.add_animal(snake)
zoo.add_animal(crocodile)
zoo.add_employee(keeper1)
zoo.add_employee(vet1)
zoo.add_employee(keeper2)
zoo.add_employee(vet2)

# Вывод информации
zoo.show_animals()
zoo.show_employees()

# Демонстрация работы сотрудников
print("\nРабота сотрудников:")
keeper1.feed_animal(lion)
vet1.heal_animal(eagle)

# Демонстрация полиморфизма
print("\nЗвуки животных:")
animal_sound(zoo.animals)