import random
from app import App
import API_Interaction as API
# NOTE: PLEASE RUN "pip install huggingface_hub" FOR API CALLS TO WORK

def main():
    app = App()
    app.mainloop()




"""
    getRandomModel is a simple function to retrieve the name of a random LLM
    models: list of tested models in string format
    Returns: Singular randomly chosen LLM name in string format
"""
def getRandomModel() -> str:
    models = ["liquid/lfm-2.5-2.6b:free",
      "nvidia/nemotron-3.5-lightning:free",
      "dots-studio/dots-3-note-preview:free",
      "google/gemma-4-26b-a4b-it:free"]
    return random.choice(models)

"""
    getRandomPrompt is a simple function for return one choice from a few predetermined prompts
    Retruns prompt in string form
"""
def getRandomPrompt()->str:
    # add prompts
    prompts = []
    return random.choice(prompts)

if __name__ == "__main__":
    main()
