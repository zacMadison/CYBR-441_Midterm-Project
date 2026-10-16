import tkinter as tk
from functools import partial
from game_screen import GameScreen
from final_screen import FinalScreen


'''
  Class App
  This class creates all the screens at the beginning, stores them in the frames dictionary, and 
  raises the frame needed to the top via the showFrames() function.
  
  This class gets the GUI going. At start up, it creates a frame called the container for where the frames will sit. 
  Any broad customization is specified there like size. Each frame inherits the container as its parent and this class
  as its controller. The screens dictionary ties a string name to the class name of the screen to use when calling showFrame. 
  But the actual screens live within the frames dictionary. showFrame() is also where the screens are raised to the top. 
  
  Research:
    The code from lines 31 to 64 is copied and slightly modified from an external source. It is the code that creates the
    screens as frames and raises them to the top when it is needed. I modified the code slightly by tying a string key to
    the class name so that a string can be passed in to the showFrames() function to make it easier. 
    
    url: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter 
'''

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("AI-dle")
    self.geometry("900x700")

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
    for name, screen in screens.items():
      frame = screen(container, self)
      self.frames[name] = frame
      frame.grid(row=0, column=0, sticky="nsew")

    self.showFrame("start_screen")

  '''
  showFrame()
    This function is used to raise the appropriate frame to the front when called
    
    Args:
        name: The name of the frame as specified in the screens dictionary
        
    Returns:
        void function
  '''

  def showFrame(self, name: str):
      frame = self.frames[name]
      if name == "game_screen":
        frame.reset()
      frame.tkraise()


'''
    Class StartScreen
    This class just puts a title and button on the first screen when starting the GUI
'''

class StartScreen(tk.Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    self.controller = controller

    title = tk.Label(self, text="AI-dle", font=("Arial", 50, "bold"))
    title.place(relx=0.5, rely=0.35, anchor="center")

    start = tk.Button(self, text="START", width="15", height="2", font=("Arial", 14), command=partial(self.controller.showFrame, "game_screen"))
    start.place(relx=0.5, rely=0.5, anchor="center")


