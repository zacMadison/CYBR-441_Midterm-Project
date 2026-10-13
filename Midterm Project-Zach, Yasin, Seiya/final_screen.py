import tkinter as tk
from functools import partial
import random

class FinalScreen(tk.Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    self.controller = controller

    title = tk.Label(self, text="Correct!", font=("Arial", 40), fg="black")
    title.place(relx=0.5, rely=0.2, anchor="center")

    your_guess = tk.Label(self, text=f"Your Guess: {getRandomPrompt()}", font=("Arial", 20), fg="black")
    your_guess.place(relx=0.25, rely=0.35, anchor="w")
    correct_guess = tk.Label(self, text=f"Correct Model: ", font=("Arial", 20), fg="black")
    correct_guess.place(relx=0.25, rely=0.5, anchor="w")

    play_again = tk.Button(self, text="PLAY AGAIN", width="15", height="2", font=("Arial", 14), command=partial(self.controller.show_frame, "game_screen"))
    play_again.place(relx=0.5, rely=0.75, anchor="center")


def getRandomPrompt() -> str:
  # add prompts
  prompts = ["This is a test", "Also a Test"]
  return str(random.choice(prompts))
