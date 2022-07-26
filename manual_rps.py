# Plays the game "Rock, Paper, Scissors" without use of a camera
import random
options = ["rock", "paper", "scissors"]

def get_computer_choice() :   # Computer randomly chooses from three options 
    global computer_choice
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice() :  # Asks user for input until they enter a valid choice
    global user_choice 
    user_choice = input("Your options are rock, paper, or scissors. What is your choice?  ")
    if user_choice in options:
        return user_choice
    else:
        print("That is not a valid choice.")
        get_user_choice() 
    return user_choice

def get_winner(computer_choice, user_choice):  # Works out who has won
    if computer_choice == user_choice :
        winner = "draw"
    elif computer_choice == "rock":
        if user_choice == "paper":
            winner = "user"
        else:
            winner = "computer"    
    elif computer_choice == "paper":
        if user_choice == "rock" :
            winner = "computer"       
        else:
            winner = "user"
    elif computer_choice == "scissors":
        if user_choice == "rock":
            winner = "user"
        else:
            winner = "computer"
    return winner

def play():  # Plays the game by running the three previous functions and printing the winner
    get_computer_choice()
    get_user_choice()
    print("The winner was: ", get_winner(computer_choice, user_choice))
      
play()        

   