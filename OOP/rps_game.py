import random

# 1 - камень, 2 - ножницы, 3 - бумага
choices = ['1', '2', '3']
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:

    correct_choice = False
    while not correct_choice:
        player_choice = input("Выберите 1 - для 'камень', 2 - для 'ножницы' или 3 - для 'бумага': ")
        if player_choice in choices:
            correct_choice = True
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    computer_choice = random.choice(choices)

    print("Вы выбрали:", player_choice)
    print("Компьютер выбрал:", computer_choice)

    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == '1' and computer_choice == '2') or (player_choice == '2' and computer_choice == '3') or (
            player_choice == '3' and computer_choice == '1'):
        print("Вы победили!")
        player_score += 1
    else:
        print("Компьютер победил!")
        computer_score += 1

    print("Ваш счет:", player_score)
    print("Счет компьютера:", computer_score)

if player_score == 3:
    print("Вы победили в игре!")
else:
    print("Компьютер победил в игре!")