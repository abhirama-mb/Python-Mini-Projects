import random as r

ROCK ='r'
PAPER = 'p'
SCISSORS = 's'
emojis = { 
    ROCK:'🪨',
    PAPER:'📰',
    SCISSORS:'✂️' 
}

choices = tuple(emojis.keys())  # choices = ('r','p','s')

wins_against = {
    ROCK: SCISSORS,   
    PAPER: ROCK, 
    SCISSORS: PAPER    
}

def get_user_choice():
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
        my_choice = get_user_choice()

        computer_choice = r.choice(choices)

        display_choices(my_choice,computer_choice)
        determine_winner(my_choice,computer_choice)
    
        if input("Press N to stop (Enter to continue): ").lower() == 'n':
            break
    

play_rps()
