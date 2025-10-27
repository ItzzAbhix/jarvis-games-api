from flask import Flask, request, jsonify
import importlib.util
import os
import sys

app = Flask(__name__)

# Get the games directory
GAMES_DIR = os.path.join(os.path.dirname(__file__), 'games')

# Available games mapping
GAMES = {
    'number_guessing': 'gn.py',
    'memory': 'mg.py',
    'math_quiz': 'mq.py',
    'riddles': 'rg.py',
    'rock_paper_scissors': 'rps.py',
    'trivia': 'tq.py'
}


class AssistantProxy:
    """Proxy class that forwards speak/listen calls to the main assistant via callbacks"""
    
    def __init__(self):
        self.speak_callback = None
        self.listen_callback = None
    
    def speak(self, text):
        """Forward speak request to main assistant"""
        if self.speak_callback:
            self.speak_callback(text)
        else:
            print(f"[Game]: {text}")
    
    def listen(self):
        """Forward listen request to main assistant"""
        if self.listen_callback:
            return self.listen_callback()
        else:
            # Fallback for testing
            return input("You: "), ""


# Global assistant proxy
assistant_proxy = AssistantProxy()


def load_game_module(game_name):
    """Dynamically load a game module"""
    if game_name not in GAMES:
        return None
    
    game_file = GAMES[game_name]
    game_path = os.path.join(GAMES_DIR, game_file)
    
    if not os.path.exists(game_path):
        return None
    
    try:
        spec = importlib.util.spec_from_file_location(game_name, game_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error loading game {game_name}: {e}")
        return None


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'online',
        'games_available': list(GAMES.keys())
    })


@app.route('/games/list', methods=['GET'])
def list_games():
    """List all available games"""
    games_info = {
        'number_guessing': 'Guess a number between 1 and 100',
        'memory': 'Remember and repeat words in sequence',
        'math_quiz': 'Answer math questions',
        'riddles': 'Solve riddles',
        'rock_paper_scissors': 'Play rock paper scissors',
        'trivia': 'Answer trivia questions'
    }
    
    return jsonify({
        'games': games_info,
        'count': len(games_info)
    })


@app.route('/games/play/<game_name>', methods=['POST'])
def play_game(game_name):
    """
    Start a game session
    This endpoint expects the desktop assistant to handle the actual game loop
    """
    if game_name not in GAMES:
        return jsonify({
            'error': 'Game not found',
            'available_games': list(GAMES.keys())
        }), 404
    
    # Load the game module
    game_module = load_game_module(game_name)
    
    if not game_module:
        return jsonify({
            'error': 'Failed to load game module'
        }), 500
    
    try:
        # Start the game with the assistant proxy
        game_module.play(assistant_proxy)
        
        return jsonify({
            'status': 'completed',
            'game': game_name
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'game': game_name
        }), 500


@app.route('/games/speak', methods=['POST'])
def game_speak():
    """
    Endpoint for games to send speech requests
    The desktop assistant should poll this or use websockets
    """
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Store the speech request for the assistant to pick up
    assistant_proxy.speak(text)
    
    return jsonify({
        'status': 'speech_queued',
        'text': text
    })


@app.route('/games/listen', methods=['POST'])
def game_listen():
    """
    Endpoint for games to request user input
    The desktop assistant should respond with the recognized speech
    """
    data = request.json
    
    # Request input from the assistant
    command, command_en = assistant_proxy.listen()
    
    return jsonify({
        'command': command,
        'command_en': command_en
    })


# ============ INTEGRATION WITH DESKTOP ASSISTANT ============

def set_speech_callback(callback):
    """Set the callback function for speech output"""
    assistant_proxy.speak_callback = callback


def set_listen_callback(callback):
    """Set the callback function for speech input"""
    assistant_proxy.listen_callback = callback


def start_game_direct(game_name, assistant_instance):
    """
    Direct integration - no HTTP needed
    This is the recommended way for local integration
    """
    if game_name not in GAMES:
        return False
    
    # Load the game module
    game_module = load_game_module(game_name)
    
    if not game_module:
        return False
    
    try:
        # Play the game directly with the assistant instance
        game_module.play(assistant_instance)
        return True
    except Exception as e:
        print(f"Error playing game: {e}")
        return False

@app.route('/')
def home():
    return jsonify({
        'status': 'Jarvis Games API is live 🚀',
        'available_endpoints': [
            '/health',
            '/games/list',
            '/games/play/<game_name>'
        ]
    })


if __name__ == '__main__':
    print("=" * 70)
    print("    GAMES API SERVER FOR JARVIS")
    print("=" * 70)
    print(f"\nGames Directory: {GAMES_DIR}")
    print(f"\nAvailable Games: {len(GAMES)}")
    for game_key, game_file in GAMES.items():
        print(f"  - {game_key} ({game_file})")
    
    print("\n" + "=" * 70)
    print("INTEGRATION METHODS:")
    print("=" * 70)
    
    print("\n1. DIRECT INTEGRATION (Recommended for local use):")
    print("   Import this module in your desktop assistant:")
    print("   >>> from Games-api.app import start_game_direct")
    print("   >>> start_game_direct('number_guessing', assistant_instance)")
    
    print("\n2. HTTP API (For remote/distributed systems):")
    print("   Start this server and make HTTP calls:")
    print("   >>> POST http://localhost:5000/games/play/number_guessing")
    
    print("\n" + "=" * 70)
    print("USAGE IN DESKTOP ASSISTANT:")
    print("=" * 70)
    
    print("\nAdd this to your desktop assistant's process_command():")
    print("""
    # Import at the top
    import sys
    sys.path.append(os.path.join(BASE_DIR, 'Games-api'))
    from app import start_game_direct
    
    # In process_command method:
    elif 'play game' in command_to_process:
        if 'number' in command_to_process or 'guessing' in command_to_process:
            self.speak("Starting number guessing game!")
            start_game_direct('number_guessing', self)
        
        elif 'memory' in command_to_process:
            self.speak("Starting memory game!")
            start_game_direct('memory', self)
        
        elif 'math' in command_to_process or 'quiz' in command_to_process:
            self.speak("Starting math quiz!")
            start_game_direct('math_quiz', self)
        
        elif 'riddle' in command_to_process:
            self.speak("Starting riddles game!")
            start_game_direct('riddles', self)
        
        elif 'rock paper scissors' in command_to_process or 'rps' in command_to_process:
            self.speak("Starting rock paper scissors!")
            start_game_direct('rock_paper_scissors', self)
        
        elif 'trivia' in command_to_process:
            self.speak("Starting trivia game!")
            start_game_direct('trivia', self)
        
        else:
            self.speak("Available games: number guessing, memory, math quiz, riddles, rock paper scissors, and trivia")
    """)
    
    print("\n" + "=" * 70)
    print("STARTING FLASK SERVER (HTTP API Mode)")
    print("=" * 70)
    print("\nServer running at: http://localhost:5000")
    print("Press Ctrl+C to stop\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)