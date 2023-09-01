# write a rock-paper-scissors game with a twist of having 5 choices instead of 3
# 1. get user input
# 2. check if the input is valid (rock, paper, scissors, lizard, spock)
# 3. if the input is not valid, ask again
# 3. get computer input
# 4. compare inputs
# 5. print the inputs from user and computer
# 6. print winner
# 7. ask to play again

import random

def get_user_input():
    user_input = input("Choose rock, paper, scissors, lizard, or spock: ")
    return user_input

def get_computer_input():
    computer_input = random.randint(1,5)
    if computer_input == 1:
        return "rock"
    elif computer_input == 2:
        return "paper"
    elif computer_input == 3:
        return "scissors"
    elif computer_input == 4:
        return "lizard"
    elif computer_input == 5:
        return "spock"
    else:
        return "error"
    

def check_input(user_input):
    if user_input == "rock" or user_input == "paper" or user_input == "scissors" or user_input == "lizard" or user_input == "spock":
        return True
    else:
        return False
    
def compare_inputs(user_input, computer_input):
    if user_input == computer_input:
        return "tie"
    elif user_input == "rock":
        if computer_input == "paper":
            return "computer"
        elif computer_input == "scissors":
            return "user"
        elif computer_input == "lizard":
            return "user"
        elif computer_input == "spock":
            return "computer"
    elif user_input == "paper":
        if computer_input == "rock":
            return "user"
        elif computer_input == "scissors":
            return "computer"
        elif computer_input == "lizard":
            return "computer"
        elif computer_input == "spock":
            return "user"
    elif user_input == "scissors":
        if computer_input == "rock":
            return "computer"
        elif computer_input == "paper":
            return "user"
        elif computer_input == "lizard":
            return "user"
        elif computer_input == "spock":
            return "computer"
    elif user_input == "lizard":
        if computer_input == "rock":
            return "computer"
        elif computer_input == "paper":
            return "user"
        elif computer_input == "scissors":
            return "computer"
        elif computer_input == "spock":
            return "user"
    elif user_input == "spock":
        if computer_input == "rock":
            return "user"
        elif computer_input == "paper":
            return "computer"
        elif computer_input == "scissors":
            return "user"
        elif computer_input == "lizard":
            return "computer"
    else:
        return "error"
    
def print_winner(winner, user_input, computer_input):

    print("You chose " + user_input)
    print("Computer chose " + computer_input)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    elif winner == "computer":
        print("Computer wins!")
    else:
        print("Error")

def play_again():
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
        return True
    else:
        return False
    
def main():
    play = True
    while play:
        user_input = get_user_input()
        while not check_input(user_input):
            print("Invalid input. Please try again.")
            user_input = get_user_input()
        computer_input = get_computer_input()
        winner = compare_inputs(user_input, computer_input)
        print_winner(winner, user_input, computer_input)
        play = play_again()
    print("Thanks for playing!")
    
main()





