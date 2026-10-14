import tkinter as tk
from functools import partial
from game_screen import GameScreen
from final_screen import FinalScreen

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("AI-dle")
    self.geometry("900x700")

  # The code in the rest of this class is code that I researched and I do have an external source that I will add on when adding official documentation
  # The idea of this code is to have frames be each screen created at startup
  # When the button to go to another screen is pressed, it is simply raised to the top

    container = tk.Frame(self)
    container.pack(fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    self.frames = {}
    screens = {
      "start_screen": StartScreen,
      "game_screen": GameScreen,
      "final_screen": FinalScreen
    }
    for name, Screen in screens.items():
      frame = Screen(container, self)
      self.frames[name] = frame
      frame.grid(row=0, column=0, sticky="nsew")

    self.show_frame("start_screen")

  def show_frame(self, name):
      frame = self.frames[name]
      if name == "game_screen":
        frame.reset()
      frame.tkraise()


# Really basic start up screen with a button programed to move onto the next screen so that I could start working on it

class StartScreen(tk.Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    self.controller = controller

    title = tk.Label(self, text="AI-dle", font=("Arial", 50, "bold"))
    title.place(relx=0.5, rely=0.35, anchor="center")

    start = tk.Button(self, text="START", width="15", height="2", font=("Arial", 14), command=partial(self.controller.show_frame, "game_screen"))
    start.place(relx=0.5, rely=0.5, anchor="center")


