import random as r

def get_user_info():
    while True:
        user_choice=input("Enter (r/p/s) : ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice")

def display_choices(my_choice,computer_choice):
    print(f"You chose: {emojis[my_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(my_choice,computer_choice):
    if my_choice == computer_choice:
        print("Its a Tie")
    elif wins_against[my_choice] == computer_choice:
        print("YOU WON ")
    else:
        print("You lost ")


def play_rps():
    print("\nWelcome to ROCK, PAPER, SCISSORS game \n")
    while True:
        my_choice = get_user_info()

        computer_choice = r.choice(choices)

        display_choices(my_choice,computer_choice)
        determine_winner(my_choice,computer_choice)
    
        if input("Press N to stop (Enter to continue): ").lower() == 'n':
            break
    
choices = ('r','p','s')

emojis = { 
    'r':'🪨',
    'p':'📰',
    's':'✂️' 
}

wins_against = {
    'r': 's',   
    'p': 'r', 
    's': 'p'    
}

play_rps()
