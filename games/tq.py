import random

def play(assistant):
    questions = [
        ("What planet is known as the Red Planet?", ["mars"]), ("Who painted the Mona Lisa?", ["leonardo", "da vinci"]),
        ("What is the capital of France?", ["paris"]), ("How many continents are there?", ["seven", "7"]),
        ("What is the largest ocean on Earth?", ["pacific"]), ("Who wrote Romeo and Juliet?", ["shakespeare"]),
        ("What is the smallest prime number?", ["two", "2"]), ("What year did World War 2 end?", ["1945", "forty five"]),
        ("What is the chemical symbol for gold?", ["au"]), ("How many sides does a hexagon have?", ["six", "6"]),
        ("What is the capital of Japan?", ["tokyo"]), ("Who invented the telephone?", ["bell", "alexander"]),
        ("What is the hardest natural substance?", ["diamond"]), ("How many colors in a rainbow?", ["seven", "7"]),
        ("What is the largest mammal?", ["blue whale", "whale"]), ("Who was the first president of USA?", ["washington", "george"]),
        ("What gas do plants absorb?", ["carbon dioxide", "co2"]), ("How many bones in human body?", ["206", "two hundred"]),
        ("What is the tallest mountain?", ["everest", "mount everest"]), ("Who wrote Harry Potter?", ["rowling", "jk"]),
        ("What is the currency of Japan?", ["yen"]), ("How many hours in a day?", ["24", "twenty four"]),
        ("What is H2O?", ["water"]), ("Who discovered gravity?", ["newton", "isaac"]),
        ("What is the capital of India?", ["delhi", "new delhi"]), ("How many planets in solar system?", ["eight", "8"]),
        ("What organ pumps blood?", ["heart"]), ("Who painted Starry Night?", ["van gogh", "gogh"]),
        ("What is the smallest country?", ["vatican"]), ("What is the capital of Australia?", ["canberra"]),
        ("Who invented the lightbulb?", ["edison", "thomas"]), ("What is the largest desert?", ["sahara"]),
        ("How many legs does a spider have?", ["eight", "8"]), ("What is the capital of Canada?", ["ottawa"]),
        ("Who wrote Pride and Prejudice?", ["austen", "jane"]), ("What is the boiling point of water?", ["100", "hundred"]),
        ("What planet is closest to the Sun?", ["mercury"]), ("Who discovered America?", ["columbus", "christopher"]),
        ("What is the capital of Russia?", ["moscow"]), ("How many sides does a triangle have?", ["three", "3"]),
        ("What is the largest planet?", ["jupiter"]), ("Who painted The Last Supper?", ["da vinci", "leonardo"]),
        ("What is the freezing point of water?", ["0", "zero"]), ("What is the capital of Egypt?", ["cairo"]),
        ("Who invented the airplane?", ["wright brothers", "wright"]), ("What is the smallest planet?", ["mercury"]),
        ("How many teeth does an adult have?", ["32", "thirty two"]), ("What is the capital of Brazil?", ["brasilia"]),
        ("Who wrote The Odyssey?", ["homer"]), ("What is the largest continent?", ["asia"]),
        ("What is the chemical symbol for water?", ["h2o"]), ("What is the capital of Spain?", ["madrid"]),
        ("Who painted Girl with Pearl Earring?", ["vermeer"]), ("What is the speed of sound?", ["343", "three forty three"]),
        ("How many minutes in an hour?", ["60", "sixty"]), ("What is the capital of Italy?", ["rome"]),
        ("Who wrote 1984?", ["orwell", "george"]), ("What is the largest island?", ["greenland"]),
        ("What is the chemical symbol for oxygen?", ["o2", "o"]), ("What is the capital of China?", ["beijing"]),
        ("Who discovered penicillin?", ["fleming", "alexander"]), ("What is the fastest land animal?", ["cheetah"]),
        ("How many states in USA?", ["50", "fifty"]), ("What is the capital of Germany?", ["berlin"]),
        ("Who wrote The Great Gatsby?", ["fitzgerald", "scott"]), ("What is the smallest bone?", ["stapes", "stirrup"]),
        ("What is the capital of Mexico?", ["mexico city"]), ("Who invented the radio?", ["marconi"]),
        ("What is the largest bird?", ["ostrich"]), ("How many seconds in a minute?", ["60", "sixty"]),
        ("What is the capital of Argentina?", ["buenos aires"]), ("Who painted The Scream?", ["munch", "edvard"]),
        ("What is the hottest planet?", ["venus"]), ("What is the capital of Turkey?", ["ankara"]),
        ("Who wrote Hamlet?", ["shakespeare", "william"]), ("What is the longest river?", ["nile", "amazon"]),
        ("How many players in cricket team?", ["11", "eleven"]), ("What is the capital of Thailand?", ["bangkok"]),
        ("Who invented the printing press?", ["gutenberg", "johannes"]), ("What is the largest fish?", ["whale shark"]),
        ("What is the capital of South Africa?", ["pretoria", "cape town"]), ("Who wrote Animal Farm?", ["orwell", "george"]),
        ("What is the smallest ocean?", ["arctic"]), ("What is the capital of Greece?", ["athens"]),
        ("Who discovered electricity?", ["franklin", "benjamin"]), ("What is the national animal of India?", ["tiger"]),
        ("How many days in a leap year?", ["366", "three sixty six"]), ("What is the capital of Portugal?", ["lisbon"]),
        ("Who wrote Macbeth?", ["shakespeare"]), ("What is the largest lake?", ["caspian"]),
        ("What is the capital of South Korea?", ["seoul"]), ("Who invented the steam engine?", ["watt", "james"]),
        ("What is the national bird of India?", ["peacock"]), ("What is the capital of Netherlands?", ["amsterdam"]),
        ("Who wrote The Catcher in the Rye?", ["salinger"]), ("What is the tallest animal?", ["giraffe"]),
        ("What is the capital of Sweden?", ["stockholm"]), ("Who invented dynamite?", ["nobel", "alfred"]),
        ("What is the largest carnivore?", ["polar bear"]), ("What is the capital of Switzerland?", ["bern"])
    ]
    
    score, total = 0, 10
    selected = random.sample(questions, total)
    
    assistant.speak(f"Trivia time! Answer {total} questions.")
    
    for i, (question, answers) in enumerate(selected, 1):
        assistant.speak(f"Question {i}: {question}")
        command, _ = assistant.listen()
        
        if any(word in command for word in ["quit", "exit", "stop"]):
            break
        
        if any(ans.lower() in command.lower() for ans in answers):
            score += 1
            assistant.speak("Correct!")
        else:
            assistant.speak(f"Wrong! Answer was {answers[0]}")
    
    assistant.speak(f"Game over! Score: {score}/{total}")