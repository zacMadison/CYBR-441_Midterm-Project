import tkinter as tk
from tkinter import ttk
import random
import API_Interaction

# Choices shown in the dropdown (same models as driver.getRandomModel())
# Can be replaced later with set_models()
MODELS = [
  "liquid/lfm-2.5-2.6b:free",
  "nvidia/nemotron-3.5-lightning:free",
  "dots-studio/dots-3-note-preview:free",
  "google/gemma-4-26b-a4b-it:free"
]

DROPDOWN_PLACEHOLDER = "Select a model"

'''
  Class GameScreen
    This class is where the frame of the game screen it located to populate the randomized prompt and model to guess.
    
    The class has a simply design layout with labels to to inform the user what is in the text box below it. When this 
    frame is called to the top the reset() function runs. This function sets a random prompt and model and then calls the 
    callAPI() function to get a response from that model to populate into the text box. The player can then choose which 
    model they believe responded from the dropdown box. When the submit button is pressed, the onSubmit() function runs.
    This function collects the player's guess and then passes their guess along with the correct model on to final_screen.py,
    where the guess will be checked and results will be shown.
    
    What is displayed on the screen:
      An Area to show the prompt that was provided to the AI
      An area to show the response that the model gave
      A dropdown box with the different models that the player can choose from
      A submit button that will take the player to FinalScreen (class within final_screen.py)
'''

class GameScreen(tk.Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)

    self.controller = controller
    self.prompt_label = ""
    self.model = ""

    self.columnconfigure(0, weight=1)
    self.rowconfigure(4, weight=1)

    # An Area to show the prompt that was provided to the AI
    title = tk.Label(self, text="Which AI Wrote This?", font=("Arial", 26, "bold"), fg="black")
    title.grid(row=0, column=0, pady=(15, 5))

    prompt_label = tk.Label(self, text="Prompt that was provided to the AI", font=("Arial", 13, "bold"), fg="black")
    prompt_label.grid(row=1, column=0, sticky="w", padx=20)

    self.prompt_text = tk.Text(self, height=3, wrap="word", font=("Arial", 12),
                               bg="#f4f4f4", relief="flat", padx=8, pady=8)
    self.prompt_text.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 8))
    self.prompt_text.config(state="disabled")  # read-only for the player

    response_label = tk.Label(self, text="Response", font=("Arial", 13, "bold"), fg="black")
    response_label.grid(row=3, column=0, sticky="w", padx=20)

    response_frame = tk.Frame(self)
    response_frame.grid(row=4, column=0, sticky="nsew", padx=20, pady=(0, 8))
    response_frame.columnconfigure(0, weight=1)
    response_frame.rowconfigure(0, weight=1)

    self.response_text = tk.Text(response_frame, wrap="word", font=("Arial", 12),
                                 bg="#f4f4f4", relief="flat", padx=8, pady=8)
    self.response_text.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(response_frame, orient="vertical", command=self.response_text.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    self.response_text.config(yscrollcommand=scrollbar.set, state="disabled")

    controls = tk.Frame(self)
    controls.grid(row=5, column=0, pady=5)

    guess_label = tk.Label(controls, text="Your guess:", font=("Arial", 12), fg="black")
    guess_label.pack(side="left", padx=(0, 8))

    self.model_var = tk.StringVar(value=DROPDOWN_PLACEHOLDER)
    self.model_dropdown = ttk.Combobox(controls, textvariable=self.model_var, values=MODELS,
                                       state="readonly", width=36, font=("Arial", 11))
    self.model_dropdown.pack(side="left", padx=(0, 10))

    self.submit_button = tk.Button(controls, text="Submit", font=("Arial", 12, "bold"),
                                   width=10, command=self.onSubmit)
    self.submit_button.pack(side="left")

    self.message_label = tk.Label(self, text="", font=("Arial", 12), fg="red")
    self.message_label.grid(row=6, column=0, pady=(0, 15))

  def setPromptText(self, prompt):
    self.setText(self.prompt_text, prompt)

  def setResponseText(self, response):
    self.setText(self.response_text, response)

  def setModels(self, models):
    self.model_dropdown.config(values=models)
    self.model_var.set(DROPDOWN_PLACEHOLDER)

  def getGuess(self) -> str | None :
    guess = self.model_var.get()
    if guess == DROPDOWN_PLACEHOLDER:
      return None
    return guess

  '''
  reset()
    This function resets the screen by getting a new random prompt and model. Then uses the new prompt and model to get 
    another response for the user to guess.
    
    ARGS: None
    RETURNS: Void
  '''

  def reset(self):
    self.prompt_label = getRandomPrompt()
    self.model = getRandomModel()
    self.setPromptText(self.prompt_label)
    self.setResponseText(API_Interaction.callAPI(self.model, self.prompt_label))
    self.model_var.set(DROPDOWN_PLACEHOLDER)
    self.message_label.config(text="")
    self.submit_button.config(state="normal")


  '''
  onSubmit()
    This function gathers the users guess and then passes it on to the final screen to check results. It runs off the frames
    implementation that was created in app.py
    
    ARGS: None
    RETURNS: Void
  '''

  def onSubmit(self):
    guess = self.getGuess()
    if guess is None:
      self.message_label.config(text="Please select a model first.")
      return
    final = self.controller.frames["final_screen"]
    final.checkResults(guess, self.model)
    self.controller.showFrame("final_screen")
    self.message_label.config(text="")


  '''
  setText()
    This function takes in a the textbox widget along side a provide text to update the text in that widget
    
    ARGS:
      widget: Read-only textbox that is being updates. For example: response_text
      text: string that will be displayed in textbox
      
    RETURNS: Void
  '''

  def setText(self, widget: tk.Text, text: str):
    widget.config(state="normal")
    widget.delete("1.0", "end")
    widget.insert("1.0", text)
    widget.config(state="disabled")

"""
    getRandomModel is a simple function to retrieve the name of a random LLM
    models: list of tested models in string format
    Returns: Singular randomly chosen LLM name in string format
"""
def getRandomPrompt() -> str:
  # add prompts
  prompts = ["Ask me a deep question", "What makes you an AI", "What is the meaning of life?", "Write me a simple program.", "What's your opinion on [Major Political Event]", "What model are you?", "Tell me a joke.", "fdl;kjnewakljbnv sadfrkjnbhgy"]
  return random.choice(prompts)


"""
    getRandomPrompt is a simple function for return one choice from a few predetermined prompts
    Returns: prompt in string form
"""
def getRandomModel() -> str:
  models = ["liquid/lfm-2.5-2.6b:free",
            "nvidia/nemotron-3.5-lightning:free",
            "dots-studio/dots-3-note-preview:free",
            "google/gemma-4-26b-a4b-it:free"]
  return random.choice(models)