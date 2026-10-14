import tkinter as tk
from functools import partial
import random

class FinalScreen(tk.Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)

    self.controller = controller
    self.guess = ""
    self.model = ""
    self.text = ""

    self.title = tk.Label(self, text="", font=("Arial", 40), fg="black")
    self.title.place(relx=0.5, rely=0.2, anchor="center")

    self.your_guess = tk.Label(self, text=f"Your Guess: ", font=("Arial", 20), fg="black")
    self.your_guess.place(relx=0.25, rely=0.35, anchor="w")
    self.correct_guess = tk.Label(self, text=f"Correct Model: ", font=("Arial", 20), fg="black")
    self.correct_guess.place(relx=0.25, rely=0.5, anchor="w")

    play_again = tk.Button(self, text="PLAY AGAIN", width="15", height="2", font=("Arial", 14), command=partial(self.controller.show_frame, "game_screen"))
    play_again.place(relx=0.5, rely=0.75, anchor="center")


  def pass_results(self, guess, model):
    self.set_model(model)
    self.set_guess(guess)
    if guess == model:
      self.title.config(text="Correct")
    else:
      self.title.config(text="Incorrect")

    self.your_guess.config(text=f"Your Guess: {guess}")
    self.correct_guess.config(text=f"Correct Model: {model}")


  def set_model(self, model):
    self.model = model

  def set_guess(self, guess):
    self.guess = guess

  def get_model(self):
    return self.model

  def get_guess(self):
    return self.guess
