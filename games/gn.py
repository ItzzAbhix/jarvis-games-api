import random
def play(assistant):
    number = random.randint(1, 100)
    attempts = 0

    assistant.speak("Welcome to the Number Guessing Game! Guess a number between 1 and 100. Your have 10 attempts.")

    while attempts < 7:
        assistant.speak(f"Attempt {attempts + 1}")
        command, _ = assistant.listen()
        
        if any(word in command for word in ["quit", "exit", "stop"]):
            assistant.speak(f"The number was {number}. Thanks for playing!")
            return
        
        try:
            guess = int(''.join(filter(str.isdigit, command)))
            attempts += 1
            
            if guess == number:
                assistant.speak(f"Correct! You won in {attempts} attempts!")
                return
            assistant.speak("Too low!" if guess < number else "Too high!")
        except:
            assistant.speak("Say a number please")
    
    assistant.speak(f"Game over! The number was {number}")