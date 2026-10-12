"""
Project Reflection – AI-dle

Project Overview
Our team built AI-dle, a desktop guessing game made with Tkinter. 
The player sees a prompt and the response an AI model gave to it, then tries to guess which model wrote the response. 
The models are Qwen, GPT-OSS, MiMo, DeepSeek, Gemma, and GLM, and we reach them through the Hugging Face Inference API. 
The point of the game is to show how different large language models really are, or aren't, from each other.

My Role
My contribution was the game screen (game_screen.py), the main screen where the game is played. 
I built a read-only area that shows the prompt sent to the AI and a scrollable, read-only area that shows the model's response. Below them, I added a dropdown listing the models the player can guess from, along with a submit button that checks a model has been selected and shows a warning if it hasn't. 
I kept the screen focused on the interface only. It doesn't call the API or decide whether a guess is right, because those parts belong to my teammates' code. 
Instead, the screen gives them a small set of methods, set_prompt(), set_response(), set_models(), get_guess(), and reset(), so the game logic can fill in the screen and read the player's guess without needing to know how the widgets are laid out. 
As the course allows, I used an AI tool to help build this interface.

Teammates' Roles
Zach M. researched, wrote, and tested API_Interaction.py, the function that sends a prompt to a chosen model through Hugging Face and returns its response. He also found the practical limits of the API, such as rate limiting and reasoning models whose think tags are left unclosed. 

Yasin built app.py, which uses a "stacked frames" pattern so each screen is created at startup and raised with show_frame(). They also built the start screen, which gave me a clear structure to plug the game screen into. 
Zach M. wrote driver.py, which launches the app and includes helper functions for picking a random model and a random prompt.

Lessons Learned
The most important lesson I learned was to keep the UI separate from the logic. At first I tried to put the API calls and the game logic straight into the game screen. That caused a circular import, because driver.py imports app.py, which imports game_screen.py. 
It also overlapped with work my teammates were already responsible for, and it went against the course rule that AI help is limited to the interface. Keeping my file UI-only made the code cleaner and the split of work clearer.

I also learned to design the screen around how other people will use it. My screen only works if my teammates' code can use it easily, so instead of hard-wiring behavior, I gave it a few simple, clearly named methods. 
Building a component for a team means thinking about the person calling your code, not just the person looking at the screen.

Another lesson was the value of agreeing early on how the pieces connect. Each of us worked on a separate file, so my screen depended on things decided elsewhere, such as the exact model names for the dropdown, which screen comes after Submit, and how the prompt and response get to my screen. 
We still need screens for correct and incorrect guesses. Talking about these points sooner would have saved rework.

Finally, Zach's testing showed me that API calls can take several seconds or fail with rate-limit errors. From that, I learned that a game screen has to handle waiting and error states, not just the case where everything succeeds.

What I Would Do Differently
If I did this project again, I would confirm with my teammates how the game screen connects to the driver and the result screens before I started coding. 
I would also test my screen with real API responses earlier, so I could see how long or messy outputs look in the response area and adjust the layout sooner.

Overall
Building the UI was harder than I expected, and it took me longer than planned to finish the game screen. 
I was new to arranging Tkinter widgets with a grid layout, making text areas read-only, and adding scrollbars, so I had to learn as I went and go through several versions before the screen worked. 
I also spent time figuring out the right scope for my file, because I first tried to include game logic that belonged in my teammates' code. 
Even though it took longer, I'm proud that the final screen is clean, easy for the rest of the team to connect to, and gave me a much better understanding of how GUI applications are built. 
Next time, I'd start the UI work earlier and check in with my teammates more often, so a slow start on my part doesn't hold up the rest of the project.

"""
