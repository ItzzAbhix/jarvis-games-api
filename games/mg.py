import random
import time

def play(assistant):
    words = [
        "apple", "ball", "cat", "dog", "elephant", "fish", "guitar", "house", "ice", "jungle",
        "kite", "lion", "moon", "nest", "ocean", "piano", "queen", "rabbit", "sun", "tree",
        "umbrella", "violin", "water", "yellow", "zebra", "book", "chair", "door", "flower", "garden",
        "heart", "island", "jacket", "key", "lamp", "mirror", "night", "orange", "pencil", "river",
        "star", "table", "valley", "window", "box", "cloud", "forest", "mountain", "rain", "tiger"
    ]
    level = 3
    
    assistant.speak("Memory game! Repeat the words in order.")
    
    while level <= 20:
        sequence = random.sample(words, level)
        
        assistant.speak(f"Level {level}. Remember {level} words:")
        time.sleep(0.5)
        
        for word in sequence:
            assistant.speak(word)
            time.sleep(1)
        
        assistant.speak("Now repeat them")
        
        for i, word in enumerate(sequence, 1):
            assistant.speak(f"Word {i}?")
            command, _ = assistant.listen()
            
            if word not in command.lower():
                assistant.speak(f"Wrong! It was {word}. You reached level {level}")
                return
        
        assistant.speak("Perfect! Next level!")
        level += 1
        time.sleep(1)
    
    assistant.speak("Amazing! You completed all levels!")