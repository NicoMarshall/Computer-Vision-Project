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
**Milestone 3:** First two milestones integrated in a separate python file to create an RPS game that gets the user choice via the camera after a 5 second countdown.
The main modules used here are Keras, numpy, cv2 and time.
```
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
    
```
The logic of the game is then coded, to work out who has won the round. First to get three wins gets overall victory.
    
```
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
 ```
 A print screen of terminal output during gameplay is shown below:
 
![image](https://user-images.githubusercontent.com/109066030/184120383-1b9cc234-9c0c-43bb-a578-f8ed73a1c58e.png)

Potential areas for improvement include printing the photograph taken by the camera each round, and adding a large countdown on the screen rather than in the terminal. 


