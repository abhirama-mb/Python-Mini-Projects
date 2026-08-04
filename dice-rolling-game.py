import random
count_times=0
while True:
    choice=input("Do you wanna roll a Dice ? (y/n) : ").lower()

    if choice=='y':
        try:
            num=int(input("GREAT!!\nHow many ? : "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if num <= 0:
            print("Please enter a positive integer.")
            continue

        count_times += num

        lst=[random.randint(1,6) for _ in range(num)]
        print("Random Numbers : ",*lst) # unpacking operator

    elif choice=='n':
        print("Thank you !")
        break
    
    else: 
        print("Invalid Choice ")

print(f"You have generated total of {count_times} random numbers.\n")


# ✅ while True: instead of while(True) (more Pythonic).
# ✅ No need to store the rolls in a list unless you need them later.
# ✅ break is preferred over exit() for ending the loop.
# ✅ Used _ as the loop variable since it isn't used.


