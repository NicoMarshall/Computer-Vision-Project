# Plays the game "Rock, Paper, Scissors" without use of a camera
import random
options = ["rock", "paper", "scissors"]

def get_computer_choice() :
    global computer_choice
    computer_choice = random.choice(options)
    return computer_choice

 
