# Основное ДЗ


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{self.name} молчит "

    def eat(self):
        return f"{self.name} ест."


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
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        for animal in self.animals:
            print(f"Зверь: {animal.name}, Возраст: {animal.age}")


# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."


# Класс Veterinarian
class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."

if __name__ == "__main__":
    # Создаем животных
    parrot = Bird("Заяц", 2)
    lion = Mammal("Лев", 5)
    snake = Reptile("Змей", 3)

    # Создаем зоопарк и добавляем животных
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    # Показываем животных в зоопарке
    zoo.show_animals()

    # Демонстрируем полиморфизм
    animal_sound(zoo.animals)

    # Создаем сотрудников зоопарка
    keeper = ZooKeeper("Управляющий Василий")
    vet = Veterinarian("Доктор Дуллитл")

    # Добавляем сотрудников в зоопарк
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Сотрудники кормят и лечат животных
    print(keeper.feed_animal(parrot))
    print(vet.heal_animal(lion))