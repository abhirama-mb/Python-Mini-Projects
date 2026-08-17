import random as r

print("\nWelcome to ROCK, PAPER, SCISSORS game \n")
emojis = { 
    'r':'🪨',
    'p':'📰',
    's':'✂️' 
}

choices = ('r','p','s')

wins_against = {
    'r': 's',   
    'p': 'r', 
    's': 'p'    
}


while True:
    my_choice=input("Enter (r/p/s) : ").lower()
    if my_choice not in choices:
        print("Invalid Choice")
        continue
        
    computer_choice = r.choice(choices)

    print(f"You chose: {emojis[my_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

    if my_choice == computer_choice:
        print("Its a Tie")
    elif wins_against[my_choice] == computer_choice:
        print("YOU WON ")
    else:
        print("You lost ")


    if input("Press N to stop (Enter to continue): ").lower() == 'n':
        break
    


