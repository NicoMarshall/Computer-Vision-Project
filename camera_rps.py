# Plays the game "Rock, Paper, Scissors" with the camera
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
import random
options = ["rock", "paper", "scissors"]

def get_computer_choice() :   # Computer randomly chooses from three options 
    global computer_choice
    computer_choice = random.choice(options)
    return computer_choice

def get_prediction():
    global prediction
    
    
    
 
    

def get_winner(computer_choice, prediction):  # Works out who has won
    if computer_choice == prediction :
        winner = "draw"
    elif computer_choice == "rock":
        if prediction == "paper":
            winner = "user"
        else:
            winner = "computer"    
    elif computer_choice == "paper":
        if prediction == "rock" :
            winner = "computer"       
        else:
            winner = "user"
    elif computer_choice == "scissors":
        if prediction == "rock":
            winner = "user"
        else:
            winner = "computer"
    return winner

def play():  
    get_computer_choice()
    get_prediction()
    print("The winner was: ", get_winner(computer_choice, prediction))
      
play()        