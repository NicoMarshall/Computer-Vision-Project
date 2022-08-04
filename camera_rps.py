# Plays the game "Rock, Paper, Scissors" with the camera
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5', compile = False)
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
import random
options = ["rock", "paper", "scissors"]


def get_computer_choice() :   # Computer randomly chooses from three options 
    global computer_choice
    computer_choice = random.choice(options)
    return computer_choice

def get_prediction(): # ML model predicts which object the user is showing to the camera
    global prediction
    counter = 0
    while counter < 6 : #counts down five seconds
        time. sleep(1)
        counter += 1
        count_down = 6 - counter
        print(count_down)
    cap = cv2.VideoCapture(0)    #takes photo
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)  #ML model gives output of 4 probabilities
    cv2.imshow('frame', frame)
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    # Find which object has the highest probability prediction 
    prediction = prediction[0].tolist()
    prediction_index = prediction.index(max(prediction))
    if prediction_index == 0:
        prediction = "rock"
    elif prediction_index == 1 :
        prediction = "paper"   
    elif prediction_index == 2 :
        prediction = "scissors"   
    else:
        prediction = "nothing"     
    print("You chose: ", prediction)    
    return prediction
    
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
               
if __name__ == '__main__':
    def play():  
        print("First to three victories. Get ready...")
        computer_wins = 0
        user_wins = 0
        while user_wins < 3 and computer_wins < 3:   #iterates game until one player has three wins
            get_computer_choice()
            get_prediction()
            print("The winner was: ", get_winner(computer_choice, prediction))
            winner = get_winner(computer_choice, prediction)
            if winner == "user":
                user_wins += 1
            elif winner == "computer":
                computer_wins += 1
        if user_wins == 3 :
            print("Congratulations, you have won!")
        elif computer_wins == 3 :
            print("Sorry, you lost")    
    play()