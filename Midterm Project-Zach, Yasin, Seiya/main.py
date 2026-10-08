import random
import API_Interaction as API
# NOTE: PLEASE RUN "pip install huggingface_hub" FOR API CALLS TO WORK

def main():
    pass




"""
    getRandomModel is a simple function to retrieve the name of a random LLM
    models: list of tested models in string format
    Returns: Singular randomly chosen LLM name in string format
"""
def getRandomModel() -> str:
    models = ["Qwen/Qwen3-Coder-480B-A35B-Instruct", "openai/gpt-oss-120b", "XiaomiMiMo/MiMo-V2.6-Pro-RL", "deepseek-ai/DeepSeek-V3.2", "google/gemma-4-31B-it", "zai-org/GLM-4.5"]
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
