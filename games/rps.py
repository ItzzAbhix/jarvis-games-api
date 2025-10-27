import random

def play(assistant):
    choices = ["rock", "paper", "scissors"]
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    score = {"you": 0, "me": 0}
    
    assistant.speak("Rock Paper Scissors! Best of 3. Say rock, paper, or scissors!")
    
    while score["you"] < 2 and score["me"] < 2:
        assistant.speak("Your choice?")
        command, _ = assistant.listen()
        
        if any(word in command for word in ["quit", "exit", "stop"]):
            break
        
        player = next((c for c in choices if c in command), None)
        if not player:
            assistant.speak("Say rock, paper, or scissors")
            continue
        
        computer = random.choice(choices)
        assistant.speak(f"I chose {computer}")
        
        if player == computer:
            assistant.speak("It's a tie!")
        elif wins[player] == computer:
            score["you"] += 1
            assistant.speak(f"You win this round! Score: You {score['you']}, Me {score['me']}")
        else:
            score["me"] += 1
            assistant.speak(f"I win this round! Score: You {score['you']}, Me {score['me']}")
    
    if score["you"] > score["me"]:
        assistant.speak("Congratulations! You won the game!")
    else:
        assistant.speak("I won! Better luck next time!")