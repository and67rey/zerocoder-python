import random

# Класс Hero
class Hero:
    def __init__(self, name, health=100, attack_power=20, attack_variation=20, block_chance=0):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.attack_variation = attack_variation
        self.block_chance = block_chance

    def attack(self, other):
        """Атакует другого героя, учитывая вариацию силы атаки."""
        if other.block_attack():
            print(f"{other.name} полностью отражает удар {self.name}!")
            return  # Урон не наносится

        variation = random.uniform(-self.attack_variation, self.attack_variation)
        damage = max(0, int(self.attack_power * (1 + variation/100)))  # Урон не меньше 0
        if other.health > damage:
            other.health -= damage
        else:
            other.health = 0
        print(f"{self.name} атакует {other.name} и наносит {damage} урона. (Сила удара: {damage})")


    def block_attack(self):
        """Проверяет, отразит ли герой удар."""
        chance = random.randint(1, 100)
        return chance <= self.block_chance

    def is_alive(self):
        """Проверяет, жив ли герой."""
        return self.health > 0


# Класс Game
class Game:
    def __init__(self, player_name, player_variation, player_block, computer_variation, computer_block, first_attack_chance=50):
        self.player = Hero(player_name, attack_variation=player_variation, block_chance=player_block)
        self.computer = Hero("Компьютер", attack_variation=computer_variation, block_chance=computer_block)
        self.first_attack_chance = first_attack_chance
        self.current_turn = self._determine_first_turn()

    def _determine_first_turn(self):
        """Определяет, кто будет атаковать первым."""
        if random.randint(1, 100) <= self.first_attack_chance:
            print(f"{self.player.name} начинает первым!")
            return "player"
        else:
            print(f"{self.computer.name} начинает первым!")
            return "computer"

    def start(self):
        print("\nИгра началась!")
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

# Ввод параметров игры
def get_settings():
    print("Добро пожаловать в игру 'Битва героев'!")
    print("Это текстовая пошаговая игра, где вы сражаетесь с компьютером, выбирая свои настройки.")
    print("Сила удара может варьироваться в заданных пределах, а также есть шанс отразить атаку противника.\n")

    player_name = input("Введите имя вашего героя: ")

    # Настройка вариации силы атаки и шанса блока
    player_variation = float(input("Введите максимальную вариацию силы удара игрока (в процентах от 0 до 50, например, 20): "))
    player_block = int(input("Введите шанс отражения атакующего удара для игрока (в процентах от 0 до 100, например, 25): "))

    computer_variation = float(input("Введите максимальную вариацию силы удара компьютера (в процентах от 0 до 50, например, 20): "))
    computer_block = int(input("Введите шанс отражения атакующего удара для компьютера (в процентах от 0 до 100, например, 25): "))

    first_attack_chance = int(input("Введите вероятность, что игрок атакует первым (в процентах от 0 до 100, например, 50): "))

    return player_name, player_variation, player_block, computer_variation, computer_block, first_attack_chance


# Запуск игры
if __name__ == "__main__":
    settings = get_settings()
    game = Game(*settings)
    game.start()
