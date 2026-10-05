# CYBR-441_Midterm-Project
AI-dle: A game where a user guesses what AI generated a response given a random prompt

## Using API_Interaction.py
  - Import API_Interaction as API (or whatever you would rather use for shorthand)
  - Call API.callAPI(model, prompt)
    - Args 
      - Model selected, list can be found in API_Interaction.py, or at the end of this document
    - prompt
      - prompt for AI, formatted as string
     
## Known Functional Models
        Qwen/Qwen3-Coder-480B-A35B-Instruct
        openai/gpt-oss-120b
        XiaomiMiMo/MiMo-V2.6-Pro-RL
        deepseek-ai/DeepSeek-V3.2
        google/gemma-4-31B-it
        zai-org/GLM-4.5
        
## Known Issues
- 429 Too Many Requests
    - This response is for a rate limit on API, if this is received wait five minutes before calling callAPI again
    
