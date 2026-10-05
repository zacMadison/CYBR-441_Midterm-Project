import os
from huggingface_hub import InferenceClient
# TOKEN: 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

# NOTE: IN ORDER TO RUN SCRIPT YOU MUST RUN "pip install huggingface_hub"
# THIS SCRIPT IS FOR FUNCTIONS RELATING TO API IMPLEMENTATION



"""
    This is a simple function for calling the hugging face inference API in order to obtain a response from of many different AI models
    Functional Models: 
        Qwen/Qwen3-Coder-480B-A35B-Instruct
        openai/gpt-oss-120b
        XiaomiMiMo/MiMo-V2.6-Pro-RL
        deepseek-ai/DeepSeek-V3.2
        google/gemma-4-31B-it
        zai-org/GLM-4.5
    
    ARGS: 
        chosen_model- Accepts strings, indicates chosen model picked from functional models listed above. The chosen model is what hugging faces inference API will return a response from
            if you pass in a model that is not listed above it may not be supported by inference providers
        prompt- Accepts strings, passed to AI language model via JSON
    
    RETURNS:
        String obtained from the "content" section of the AI response, which is the actual response stripped of other context (such as initial user message)
        
    KNOWN ISSUES:
        If too requests are made you will get: "429 Too Many Requests for url: https://router.huggingface.co/v1/chat/completions." 
            If you get this error wait 5 minutes before trying again.
        Reasoning models cannot be used, <think> tags will frequently be unclosed, and therefore impossible to remove
  
    FUNCTION CONTRIBUTORS:
        Zach M.- reasearch, scripting, and testing
"""
def callAPI( chosen_model:str, prompt:str)->str:
    client = InferenceClient(provider="auto", token="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")
    text = client.chat.completions.create(
        model=chosen_model,
        messages=[
           
            {
        
                "role":"system",
                "content": "Do not mention who you are or who made you, otherwise respond normally. "
            },
            {
                "role":"user",
                "content": prompt
            }

        ]
        
    )
    return text.choices[0].message.content

