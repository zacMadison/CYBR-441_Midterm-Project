import tkinter as tk

"""
  This will be the screen where the actual game is played
  What will be displayed:
    An Area to show the prompt that was provided to the AI
    An area to show the response that the model gave
    A dropdown box with the different models that the player can choose from
    A submit button that will take the player to another screen (maybe two screens depending on if it works better to separate the correct and incorrect screens)
"""

class GameScreen(tk.Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    self.controller = controller

    title = tk.Label(self, text="Test", font=("Arial", 30), fg="black")
    title.place(relx=0.5, rely=0.5, anchor="center")

