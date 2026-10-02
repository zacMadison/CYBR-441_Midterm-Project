import os
from huggingface_hub import InferenceClient
# TOKEN: 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
# NOTE: IN ORDER TO RUN SCRIPT YOU MUST RUN "pip install huggingface_hub"
# ALL CONTENT IS CURRENTLY FOR TESTING AND WILL BE CHANGED LATER


# This function is for testing, this function will not have a main
def main():
    callAPI()
    pass

def callAPI():
    client = InferenceClient(provider="auto", token="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")
    text = client.chat.completions.create(
        model="XiaomiMiMo/MiMo-V2.6-Pro-RL",
        messages=[
            {
                "role":"user",
                "content": "Hey, this is a test prompt, what do you think?"
            }
        ]
    )
    print(text.choices[0].message)


if __name__ == "__main__":
    main()
