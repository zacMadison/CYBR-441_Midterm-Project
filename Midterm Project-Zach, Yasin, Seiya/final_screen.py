import tkinter as tk
from functools import partial

'''
  Class FinalScreen:
    This class is the frame for the last screen that shows results from the guess.
    
    This class pulls in the user's guess and correct model to compare and determine if the user was correct.
    The screen will show your guess as well as the correct model and then show whether or not your were correct.
'''

class FinalScreen(tk.Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)

    self.controller = controller
    self.guess = ""
    self.model = ""
    self.text = ""

    self.title = tk.Label(self, text="", font=("Arial", 40), fg="black")
    self.title.place(relx=0.5, rely=0.2, anchor="center")
    self.your_guess = tk.Label(self, text="Your Guess: ", font=("Arial", 20), fg="black")
    self.your_guess.place(relx=0.25, rely=0.35, anchor="w")
    self.correct_guess = tk.Label(self, text="Correct Model: ", font=("Arial", 20), fg="black")
    self.correct_guess.place(relx=0.25, rely=0.5, anchor="w")
    play_again = tk.Button(self, text="PLAY AGAIN", width="15", height="2", font=("Arial", 14), command=partial(self.controller.showFrame, "game_screen"))
    play_again.place(relx=0.5, rely=0.75, anchor="center")


  ''' 
  checkResults()
    This function takes in the players guess and the correct model to check and determine if they were correct.
  
      Args:
          guess: The guess that the player made
          model: The model that was selected from the getRandomModel() function
          
      Returns: 
          Void function
  '''
  def checkResults(self, guess: str, model: str):
    self.set_model(model)
    self.set_guess(guess)
    if guess == model:
      self.title.config(text=f"Correct")
    else:
      self.title.config(text=f"Incorrect")

    self.your_guess.config(text=f"Your Guess: {guess}")
    self.correct_guess.config(text=f"Correct Model: {model}")


  def set_model(self, model: str):
    self.model = model

  def set_guess(self, guess: str):
    self.guess = guess

  def get_model(self) -> str:
    return self.model

  def get_guess(self) -> str:
    return self.guess
