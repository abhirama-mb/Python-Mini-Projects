from random import randint 

random_num = randint(1,1000)
count_times=0

while True:
    guess=int(input("Guess the Number : "))
    count_times += 1

    if guess == random_num:
        print("\nCongratulations!")
        print(f"You guessed {guess} correctly.")
        print(f"It took you {count_times} attempts.")
        if count_times <= 10 :
            print("Impressive! You probably used a Binary Search approach.")
        print("Thank you!\n")
        break

    if guess > random_num :
        print("High !! Try again")
    else :
        print("Low !! Try again")

# try to add exceptional handling