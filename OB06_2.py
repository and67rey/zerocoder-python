import random

# Класс Hero
class Hero:
    def __init__(self, name, health=100, attack_power=20, attack_variation=0.5):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.attack_variation = attack_variation

    def attack(self, other):
        """Метод для атаки. Урон фиксированный, без вариаций."""
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        """Проверяет, жив ли герой."""
        return self.health > 0

# Класс PlayerHero (с учетом вариации силы удара)
class PlayerHero(Hero):
    def attack(self, other):
        """Метод для атаки с учетом случайной вариации силы удара."""
        variation = random.uniform(-self.attack_variation, self.attack_variation)  # Используем attack_variation
        damage = max(0, int(self.attack_power * (1 + variation)))  # Урон не меньше 0
        if other.health > damage:
            other.health -= damage
        else:
            other.health = 0
        print(f"{self.name} атакует {other.name} и наносит {damage} урона. (Сила удара: {damage})")

# Класс Game
class Game:
    def __init__(self, player_name):
        self.player = PlayerHero(player_name, attack_variation=0.5)  # Игрок с вариацией
        self.computer = PlayerHero("Компьютер", attack_variation=0.5)      # Компьютер с вариацией

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
