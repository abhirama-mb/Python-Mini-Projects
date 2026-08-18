import random


def get_choice():
    while True:
        choice = input("Do you wanna roll a Dice? (y/n): ").lower()

        if choice in ('y', 'n'):
            return choice

        print("Invalid Choice")


def get_number_of_dice():
    while True:
        try:
            num = int(input("GREAT!!\nHow many?: "))

            if num > 0:
                return num

            print("Please enter a positive integer.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


def roll_dice(num):
    return [random.randint(1, 6) for _ in range(num)]


def display_rolls(rolls):
    print("Random Numbers:", *rolls)


def play_game():
    count_times = 0

    while True:
        choice = get_choice()

        if choice == 'n':
            print("Thank you!")
            break

        num = get_number_of_dice()
        count_times += num

        rolls = roll_dice(num)
        display_rolls(rolls)

    print(f"You have generated total of {count_times} random numbers.")


play_game()