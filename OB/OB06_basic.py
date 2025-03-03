import random

# Класс Hero
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0

# Класс Game
class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        print(f"{self.player.name} VS {self.computer.name}")
        print()

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            self._print_health()
            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            self._print_health()
            if not self.player.is_alive():
                print(f"{self.computer.name} побеждает!")
                break

    def _print_health(self):
        print(f"{self.player.name}: {self.player.health} здоровья")
        print(f"{self.computer.name}: {self.computer.health} здоровья")
        print("-" * 30)

# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
