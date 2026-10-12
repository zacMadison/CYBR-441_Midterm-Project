import tkinter as tk
from tkinter import ttk
# TODO: populate gamescreen with information from API 
"""
  This will be the screen where the actual game is played
  What will be displayed:
    An Area to show the prompt that was provided to the AI
    An area to show the response that the model gave
    A dropdown box with the different models that the player can choose from
    A submit button that will take the player to another screen (maybe two screens depending on if it works better to separate the correct and incorrect screens)
"""

# Choices shown in the dropdown (same models as driver.getRandomModel())
# Can be replaced later with set_models()
MODELS = [
  "liquid/lfm-2.5-2.6b:free",
  "nvidia/nemotron-3.5-lightning:free",
  "dots-studio/dots-3-note-preview:free",
  "google/gemma-4-26b-a4b-it:free"
]

DROPDOWN_PLACEHOLDER = "Select a model"

class GameScreen(tk.Frame):
  def __init__(self, parent, controller):
    super().__init__(parent)
    self.controller = controller

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
                                   width=10, command=self.on_submit)
    self.submit_button.pack(side="left")

    self.message_label = tk.Label(self, text="", font=("Arial", 12), fg="red")
    self.message_label.grid(row=6, column=0, pady=(0, 15))

  def set_prompt(self, prompt):
    self.set_text(self.prompt_text, prompt)

  def set_response(self, response):
    self.set_text(self.response_text, response)

  def set_models(self, models):
    self.model_dropdown.config(values=models)
    self.model_var.set(DROPDOWN_PLACEHOLDER)

  def get_guess(self):
    guess = self.model_var.get()
    if guess == DROPDOWN_PLACEHOLDER:
      return None
    return guess

  def reset(self):
    self.set_prompt("")
    self.set_response("")
    self.model_var.set(DROPDOWN_PLACEHOLDER)
    self.message_label.config(text="")
    self.submit_button.config(state="normal")


  def on_submit(self):
    guess = self.get_guess()
    if guess is None:
      self.message_label.config(text="Please select a model first.")
      return

    self.message_label.config(text="")

  def set_text(self, widget, text):
    widget.config(state="normal")
    widget.delete("1.0", "end")
    widget.insert("1.0", text)
    widget.config(state="disabled")
