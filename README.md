# Computer-Vision-Project
Training a machine learning model to play rock, paper, scissors using a laptop camera.

**Milestone 1:** The ML model is created and trained on TeachableMachine (https://teachablemachine.withgoogle.com/train/image). Four image classes were created (rock, paper, scissors, nothing) 
and given images from my webcam, corresponding to the object of the class, with approximately 50 images for each class.
This model will later be used to interpret user image input in the game "Rock, Paper, Scissors".

**Milestone 2:** A manual RPS game is coded in python i.e no camera input is used. The computer randomly chooses from the 3 options, the user is asked for an input and 
the two choices are compared to evaluate who won. The winner is printed:

```
def play():  # Plays the game by running the three previous functions and printing the winner
    get_computer_choice()
    get_user_choice()
    print("The winner was: ", get_winner(computer_choice, user_choice))

```

