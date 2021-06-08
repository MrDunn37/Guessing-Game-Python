"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    print("Hello, welcome to the guessing game my friend? Dare to try your luck???")
    name = input("What do they call you friend? ")
    answer = random.randint(1,10)
    total_guesses = 1
    try:
      guess = int(input("Pick a number between 1 and 10 {} ".format(name)))
    except ValueError as err:
      print("So {}, I assume this is your first time playing a guessing game.  I neeed a WHOLE NUMBER ONLY BETWEEN 1 AND 10 MY FRIEND!".format(name))
    else:
      while guess != answer:
        if guess > 10:
          print("Sorry {}, you guess cannot be larger than 10".format(name))
          guess = int(input("Pick a number between 1 and 10 {} ".format(name)))
        elif guess <0:
          print("Sorry {}, you guess cannot be smaller than 0".format(name))
          guess = int(input("Pick a number between 1 and 10 {} ".format(name)))
        elif guess > answer:
          print("{}, it's lower".format(name))
          guess = int(input("Pick a number between 1 and 10 {} ".format(name)))
          total_guesses += 1
        elif guess < answer:
          print("{}, it's higher".format(name))
          guess = int(input("Pick a number between 1 and 10 {} ".format(name)))
          total_guesses += 1
        else:
          if guess == answer:
            break
      print(("Good Job {},you got it! The correct number was ".format(name) + str(answer) +  " and it took you a total of "+ str(total_guesses) + " guesses"))
      print("Thanks for coming to play today, next time your feeling lucky come back and pay me another visit!")
    
# Kick off the program by calling the start_game function.
start_game()