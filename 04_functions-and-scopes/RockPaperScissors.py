# Code a rock paper scissors game
# Take in a number 0-2 from the user that represents their hand
# Generate a random number 0-2 to use for the computer's hand
# Call the function get_hand to get the string representation of the user's hand
# Call the functin get_hand to get the string representation of the compunter's hand
# Call the function determine_winner to figure out who won
# Print out the player hand and computer hand
# Print out the winner

import random

user_num = int(input("Please enter a 0, 1, or 2: "))

computer_num = random.randint(0,2)

def get_hand(num):
    if num == 0:
        return "rock"
    elif num == 1:
        return "paper"
    elif num == 2:
        return "scissors"

user_tool = get_hand(user_num)
computer_tool = get_hand(computer_num)
user_winner = False

def determine_winner(first_tool, second_tool):
    print(f"You played: {first_tool} \n")
    print(f"The computer played: {second_tool} \n")

    if first_tool == second_tool:
        return "It's a tie"
    elif first_tool == "rock" and second_tool == "scissors":
        user_winner = True
        return "Rock crushes scissors, you win!"
    elif first_tool == "rock" and second_tool == "paper":
        return "Paper covers rock, you loose!"
    elif first_tool == "paper" and second_tool == "rock":
        user_winner = True
        return "Paper covers rock, you win!"
    elif first_tool == "paper" and second_tool == "scissors":
        return "Scissors cut paper, you loose!"
    elif first_tool == "scissors" and second_tool == "rock":
        return "Rock crushes scissors, you loose!"
    elif first_tool == "scissors" and second_tool == "paper":
        user_winner = True
        return "Scissors cut paper, you win!"

winner_hand = determine_winner(user_tool, computer_tool)
print(winner_hand)

if user_winner == True:
    print("Congratulations!!")
else:
    print("Better luck next time!")