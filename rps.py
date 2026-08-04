import random as r

print("\nWelcome to ROCK, PAPER, SCISSORS game \n")
choices = ('r','p','s')

while True:
    my_choice=input("Enter (r/p/s) : ").lower()
    if my_choice not in choices:
        print("Invalid Choice")
        continue
        
    computer_choice=r.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if my_choice == 'r' :
        if computer_choice == 's':
            print("you won")
        elif computer_choice == 'p':
            print("you lost")
        else:
            print("Tie")

    elif my_choice == 'p':
        if computer_choice == 'r':
            print("you won")
        elif computer_choice == 's':      
            print("you lost")
        else:
            print("Tie")

    elif my_choice == 's':
        if computer_choice == 'p':
            print("you won")
        elif computer_choice == 'r':      
            print("you lost")
        else:
            print("Tie")

    if input("Wanna Play again ? (y/n) : ").lower() == 'n':
        break
    


