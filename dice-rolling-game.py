import random
while True:
    choice=input("Do you wanna roll a Dice ? (y/n) : ").lower()

    if choice=='y':

        num=int(input("GREAT!!\nHow many ? : "))
        lst=[]

        for _ in range(num):
            lst.append(random.randint(1,6))

        for i in range(num):
            print(lst[i])

    elif choice=='n':
        print("Thank you !")
        break
    
    else: 
        print("Invalid Choice ")


# ✅ while True: instead of while(True) (more Pythonic).
# ✅ No need to store the rolls in a list unless you need them later.
# ✅ break is preferred over exit() for ending the loop.
# ✅ Used _ as the loop variable since it isn't used.