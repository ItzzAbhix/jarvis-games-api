import random

def play(assistant):
    riddles = [
        ("I speak without a mouth and hear without ears. What am I?", ["echo"]),
        ("What has keys but no locks, space but no room?", ["keyboard"]),
        ("What gets wet while drying?", ["towel"]),
        ("What can travel around the world while staying in a corner?", ["stamp"]),
        ("The more you take, the more you leave behind. What am I?", ["footsteps", "steps"]),
        ("What has a head and tail but no body?", ["coin"]),
        ("What has hands but cannot clap?", ["clock", "watch"]),
        ("What goes up but never comes down?", ["age"]),
        ("I'm light as a feather, yet strongest person can't hold me five minutes. What am I?", ["breath"]),
        ("What has 88 keys but can't open a door?", ["piano"]),
        ("What runs but never walks, has a mouth but never talks?", ["river"]),
        ("What can you catch but never throw?", ["cold", "illness"]),
        ("What has one eye but cannot see?", ["needle"]),
        ("What belongs to you but others use it more?", ["name"]),
        ("What comes once in a minute, twice in a moment, never in a thousand years?", ["m", "letter m"]),
        ("What has cities but no houses, forests but no trees, water but no fish?", ["map"]),
        ("What gets bigger the more you take away?", ["hole"]),
        ("I have branches but no fruit, trunk, or leaves. What am I?", ["bank"]),
        ("What can fill a room but takes up no space?", ["light"]),
        ("The more of this there is, the less you see. What is it?", ["darkness", "dark"]),
        ("What can run but never walks, has a bed but never sleeps?", ["river"]),
        ("What has a neck but no head?", ["bottle"]),
        ("What goes through towns and hills but never moves?", ["road"]),
        ("What has words but never speaks?", ["book"]),
        ("What has four legs but cannot walk?", ["table", "chair"]),
        ("What can be broken without being held?", ["promise"]),
        ("What has a ring but no finger?", ["phone", "telephone"]),
        ("What gets sharper the more you use it?", ["brain", "mind"]),
        ("What goes around the house but never moves?", ["fence", "wall"]),
        ("What has teeth but cannot bite?", ["comb", "saw"]),
        ("What can be opened but never closed?", ["egg"]),
        ("What has a face but no body?", ["clock"]),
        ("What building has the most stories?", ["library"]),
        ("What gets answered without a question?", ["door", "doorbell"]),
        ("What has many needles but doesn't sew?", ["pine tree", "christmas tree"]),
        ("What kind of room has no doors or windows?", ["mushroom"]),
        ("What runs around a yard without moving?", ["fence"]),
        ("What has bark but no bite?", ["tree"]),
        ("What has a bottom at the top?", ["leg", "legs"]),
        ("What can travel faster than light?", ["shadow", "darkness"]),
        ("What has an eye but cannot see you back?", ["storm", "hurricane"]),
        ("What disappears when you say its name?", ["silence"]),
        ("What invention lets you look through walls?", ["window"]),
        ("What begins with T, ends with T, has T in it?", ["teapot"]),
        ("What is always in front of you but can't be seen?", ["future"]),
        ("What is full of holes but still holds water?", ["sponge"]),
        ("What question can you never answer yes to?", ["are you asleep", "asleep"]),
        ("What breaks but never falls?", ["day", "dawn"]),
        ("What falls but never breaks?", ["night", "waterfall"]),
        ("What has no life but can die?", ["battery"])
    ]
    
    score, total = 0, 10
    selected = random.sample(riddles, total)
    
    assistant.speak(f"Riddle time! Solve {total} riddles.")
    
    for i, (riddle, answers) in enumerate(selected, 1):
        assistant.speak(f"Riddle {i}: {riddle}")
        command, _ = assistant.listen()
        
        if any(word in command for word in ["quit", "exit", "stop"]):
            break
        
        if any(ans in command.lower() for ans in answers):
            score += 1
            assistant.speak("Correct!")
        else:
            assistant.speak(f"Wrong! Answer was {answers[0]}")
    
    assistant.speak(f"Game over! Score: {score}/{total}")