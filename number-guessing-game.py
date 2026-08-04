from random import randint 

print("\nGuess the Number from 1 to 1000\n")

random_num = randint(1,1000)
count_times=0

while True:
    try:
        guess=int(input("Guess the Number : "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        continue

    count_times += 1

    if not 1 <= guess <= 1000:
        print("Please enter a number between 1 and 1000.")
        continue

    if guess == random_num:
        print("\nCongratulations!")
        print(f"You guessed {guess} correctly.")
        print(f"It took you {count_times} attempts.")
        if count_times <= 10 :
            print("Impressive! You probably used a Binary Search approach.")
        print("Thank you!\n")
        break

    elif guess > random_num:
        print("High !! Try again")

    else :
        print("Low !! Try again")

