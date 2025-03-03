from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self):
        super().__init__("Меч", "Острое клинковое оружие, эффективное в ближнем бою.")

    def attack(self):
        return "наносит удар мечом!"

class Bow(Weapon):
    def __init__(self):
        super().__init__("Лук", "Дальнобойное оружие, использующее стрелы.")

    def attack(self):
        return "стреляет из лука!"

class MagicWand(Weapon):
    def __init__(self):
        super().__init__("Волшебная палочка", "Магический инструмент, создающий заклинания.")

    def attack(self):
        return "использует волшебную палочку!"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.name}.")
        print(f"{weapon.name}: {weapon.description}\n")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}")
        else:
            print(f"{self.name} не вооружён!")

class Monster:
    def __init__(self, name):
        self.name = name

    def defeated(self):
        print(f"Монстр {self.name} побеждён!\n")


# Создание объектов
fighter = Fighter("Герой")
monster = Monster("Дракон")

# Выбор меча
sword = Sword()
fighter.change_weapon(sword)
fighter.attack()
monster.defeated()

# Выбор лука
bow = Bow()
fighter.change_weapon(bow)
fighter.attack()
monster.defeated()

# Добавление нового оружия
magic_wand = MagicWand()
fighter.change_weapon(magic_wand)
fighter.attack()
monster.defeated()
