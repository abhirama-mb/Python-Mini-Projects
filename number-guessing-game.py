from random import randint


def get_guess():
    while True:
        try:
            guess = int(input("Guess the Number : "))

            if 1 <= guess <= 1000:
                return guess

            print("Please enter a number between 1 and 1000.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


def check_guess(guess, random_num):
    if guess == random_num:
        return "correct"
    elif guess > random_num:
        return "high"
    else:
        return "low"


def display_result(guess, result):
    if result == "correct":
        print("\nCongratulations!")
        print(f"You guessed {guess} correctly.")
    elif result == "high":
        print("High !! Try again")
    else:
        print("Low !! Try again")


def play_game():
    print("\nGuess the Number from 1 to 1000\n")

    random_num = randint(1, 1000)
    count_times = 0

    while True:
        guess = get_guess()
        count_times += 1

        result = check_guess(guess, random_num)
        display_result(guess, result)

        if result == "correct":
            print(f"It took you {count_times} attempts.")

            if count_times <= 10:
                print("Impressive! You probably used a Binary Search approach.")

            print("Thank you!\n")
            break


play_game()