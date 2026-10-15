import os
import requests
import json
# TOKEN: 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




"""
    This is a simple function for calling the OpenRouter API in order to obtain a response from of many different AI models
    Functional Models: 
        liquid/lfm-2.5-2.6b:free
        nvidia/nemotron-3.5-lightning:free
        dots-studio/dots-3-note-preview:free
        google/gemma-4-26b-a4b-it:free
    
    ARGS: 
        model- Accepts strings, indicates chosen model picked from functional models listed above. The chosen models are what OpenRouter API will return a response from
            if you pass in a model that is not listed above it may not be supported by inference providers
        prompt- Accepts strings, passed to AI language model via JSON
    
    RETURNS:
        String obtained from the "content" section of the AI response, which is the actual response stripped of other context (such as initial user message)
        
    KNOWN ISSUES:
        Google Gemma is prone to rate limits, to mitigate this it is being rerouted to seperate freetier api endpoint in google ailabs
  
    FUNCTION CONTRIBUTORS:
        Zach M.- reasearch, scripting, and testing
"""
def callAPI( model:str, prompt:str)->str:
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": model,
            "messages": [
                {
                "role": "system",
                "content": "Do not mention who you are or who made you, otherwise respond normally."
                },
                {
                "role": "user",
                "content": prompt
                }
            ],
            "reasoning": {"enabled": True}
        })
    )
    parsed_response = response.json()
    if "error" in parsed_response:
        return "ERROR: This model either cannot be reached at the moment or is under a rate limit"
    parsed_response = parsed_response["choices"][0]["message"]["content"]

    return parsed_response


