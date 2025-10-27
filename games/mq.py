import random
import operator

def play(assistant):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    score = 0
    total = 5
    
    assistant.speak(f"Math quiz time! Answer {total} questions.")
    
    for i in range(total):
        a, b = random.randint(1, 20), random.randint(1, 20)
        op_symbol = random.choice(list(ops.keys()))
        answer = ops[op_symbol](a, b)
        
        assistant.speak(f"Question {i+1}: What is {a} {op_symbol} {b}?")
        command, _ = assistant.listen()
        
        if any(word in command for word in ["quit", "exit", "stop"]):
            break
        
        try:
            user_answer = int(''.join(filter(str.isdigit, command.replace("minus", "-"))))
            if user_answer == answer:
                score += 1
                assistant.speak("Correct!")
            else:
                assistant.speak(f"Wrong! The answer was {answer}")
        except:
            assistant.speak(f"Invalid answer. The correct answer was {answer}")
    
    assistant.speak(f"Quiz over! You scored {score} out of {total}")