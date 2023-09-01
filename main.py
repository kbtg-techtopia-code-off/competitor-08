# write a rock-paper-scissors game
# 1. get user input
# 2. check if the input is valid
# 3. if the input is not valid, ask again
# 3. get computer input
# 4. compare inputs
# 5. print the inputs from user and computer
# 6. print winner
# 7. ask to play again

import random

def get_user_input():
    user_input = input("Please input your choice [rock, paper, or scissors]: ")
    return user_input

def get_computer_input():
    computer_input = random.randint(0, 2)
    if computer_input == 0:
        computer_input = "rock"
    elif computer_input == 1:
        computer_input = "paper"
    else:
        computer_input = "scissors"
    return computer_input

def check_input(user_input):
    if user_input == "rock" or user_input == "paper" or user_input == "scissors":
        return True
    else:
        return False
    
def compare_inputs(user_input, computer_input):

    if user_input == computer_input:
        return "tie"
    elif user_input == "rock" and computer_input == "paper":
        return "computer"
    elif user_input == "rock" and computer_input == "scissors":
        return "user"
    elif user_input == "paper" and computer_input == "rock":
        return "user"
    elif user_input == "paper" and computer_input == "scissors":
        return "computer"
    elif user_input == "scissors" and computer_input == "rock":
        return "computer"
    elif user_input == "scissors" and computer_input == "paper":
        return "user"
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





