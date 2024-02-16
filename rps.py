import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"\nEnter a choice ({choices_str}): "))
    action = Action(selection)
    return action


def get_computer_selection():
    selection = random.randint(1, len(Action))
    action = Action(selection)
    return action

def get_winner(user_action, computer_action):
    winner = {
        Action.Rock: [Action.Scissors], # Rock beats Scissors
        Action.Paper: [Action.Rock], # Paper beats rock
        Action.Scissors: [Action.Paper], # Scissors beats paper
    }

    loser = winner[user_action]
    if user_action == computer_action:
        print(f"\nBoth players selected {user_action.name}. It's a TIE!!")
    elif computer_action in loser:
        print(f"\n{user_action.name} beats {computer_action.name}! You WIN!!")
    else: 
        print(f"\n{computer_action.name} beats {user_action.name}! You LOSE!!")


def play():
    print()
    print('==== GAME STARTS NOW ======== \n'
        + "Winning rules of the game ROCK PAPER SCISSORS are :\n"
        + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissors -> Rock wins \n"
        + "Paper vs Scissors -> Scissor wins \n"
        + "============================= \n")

    while True:
        try:
            user_action = get_user_selection()
        except ValueError as e:
            range_str = f"[1, {len(Action)}]"
            print(f"\nInvalid selection. Enter a value in range {range_str}")
            continue

        computer_action = get_computer_selection()
        get_winner(user_action, computer_action)

        play_again = input("\nPlay again? (y/n): ")
        if play_again.lower() != "y":
            break

    
    print("\nGoodBye!! Thanks for playing")


play()