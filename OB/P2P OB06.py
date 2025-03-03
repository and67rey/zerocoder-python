
import random

# Класс Hero: Основной базовый класс для всех героев
class Hero:
    # Атрибуты, характеристики класса
    def __init__(self, name):
        self.name = name
        self.health = 100 # Здоровье
        self.attack_power = 20 # Сила удара

    # Метод, действия класса
    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} наносит удар по {other.name}. \nУ {other.name} осталось {other.health} здоровья.")

    # Метод, действия класса (если жив?)
    def is_alive(self):
        return self.health > 0

# Класс Game: класс, управляющий логикой игры.
class Game:
    # Атрибуты, характеристики класса Game
    def __init__(self, player):
        self.player = Hero(player)
        self.computer = Hero("Компьютер")

    #метод start класса Game, который управляет ходами и выводить результат.
    def start(self):
        print("\nЗапуск игры!")
        # Цикл определяющий победителя
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]): # кто начинает?
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)
            # Вывод на консоль победителя
            if not self.computer.is_alive():
                print(f"\n{self.computer.name} побеждён! {self.player.name} победил!")
                break
            elif not self.player.is_alive():
                print(f"\n{self.player.name} побеждён! {self.computer.name} победил!")
                break

# Выбор имени игрока и запуск игры
name_1 = input("Введите имя вашего игрока: ")
game = Game(name_1)
game.start()