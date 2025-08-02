from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
import google.generativeai as genai
import sys

app = Flask(__name__)
CORS(app)

# --- PASTE YOUR API KEY HERE ---
# Replace with your actual API key or use environment variable
API_KEY = os.getenv('GEMINI_API_KEY', "AIzaSyCKrMXxF9T2uRtpjQlGLGbk0J-fZHIi7Ic")

class KeanuPhilosophicalAI:
    def __init__(self):
        """Initialize Keanu's philosophical wisdom with Gemini configuration"""
        try:
            genai.configure(api_key=API_KEY)
            self.model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
            self.configured = True
            print("✓ Keanu's wisdom is now available")
        except Exception as e:
            print(f"✗ Error configuring Gemini API: {e}")
            self.configured = False
    
    def get_philosophical_quote(self, question):
        """
        Channels Keanu's philosophical wisdom through Gemini API
        """
        if not self.configured:
            return "The matrix has encountered an error. Please check the API configuration, dude."
        
        # Enhanced prompt that captures Keanu's philosophical style
        prompt_text = f"""You are channeling the philosophical wisdom of Keanu Reeves. Respond to questions with deep, thoughtful wisdom that reflects Keanu's known philosophical outlook and his humble, contemplative nature.

Your response should:
- Be genuinely wise and thoughtful like Keanu would be
- Include his characteristic humility and depth
- Be philosophical but accessible
- Sound like something Keanu might actually say in an interview
- Be 1-3 sentences of profound insight
- Avoid clichés and be authentic

User question: "{question}"

Keanu's wise response:"""

        try:
            # Generate the content from the model
            response = self.model.generate_content(prompt_text)

            # Return the generated text
            if response.candidates and response.text:
                # Clean up the response
                wisdom = response.text.strip()
                if wisdom.startswith('"') and wisdom.endswith('"'):
                    wisdom = wisdom[1:-1]
                return wisdom
            else:
                return "Sometimes the most profound answer is silence. But not this time - try asking again, friend."

        except Exception as e:
            return f"The universe is having technical difficulties right now: {str(e)}"

# Initialize Keanu's AI
keanu = KeanuPhilosophicalAI()

@app.route('/')
def index():
    """Serve the main Keanu interface"""
    return render_template('index.html')

@app.route('/llm', methods=['POST'])
def llm():
    """Handle LLM requests from the Keanu frontend"""
    try:
        data = request.json
        
        # Validate input - your frontend sends 'question' field
        if not data or 'question' not in data:
            return jsonify({
                'response': 'You need to ask a question first, my friend.',
                'error': True
            }), 400
            
        user_question = data.get('question', '').strip()
        
        if not user_question:
            return jsonify({
                'response': 'Silence is golden, but I need a question to share some wisdom.',
                'error': True
            }), 400
        
        print(f"User question: {user_question}")
        
        # Get response from Keanu's philosophical AI
        keanu_wisdom = keanu.get_philosophical_quote(user_question)
        
        print(f"Keanu's wisdom: {keanu_wisdom}")
        
        return jsonify({
            'response': keanu_wisdom
        })
        
    except Exception as e:
        print(f"Error in LLM endpoint: {str(e)}")
        return jsonify({
            'response': 'Something went wrong in the matrix. Try again, and remember - there is no spoon.',
            'error': True
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Keanu Philosophical AI',
        'keanu_ready': keanu.configured,
        'api_configured': API_KEY != "YOUR_API_KEY_HERE"
    })

@app.route('/api/wisdom', methods=['GET'])
def get_random_wisdom():
    """Get a random piece of Keanu wisdom"""
    keanu_quotes = [
        "The simple act of paying attention can take you a long way.",
        "Grief changes shape, but it never ends.",
        "Every struggle in your life has shaped you into the person you are today.",
        "The person who was holding me back from my happiness was me.",
        "Art is about trying to find the good in people and making the world a more compassionate place.",
        "I try not to think about my life. I have no regrets. You learn from everything and move on.",
        "When the people you love are gone, you are alone. But if you live your life right, their love stays with you."
    ]
    
    import random
    wisdom = random.choice(keanu_quotes)
    
    return jsonify({
        'wisdom': wisdom,
        'status': 'success'
    })

# Route to serve static files (CSS, JS) if they're in the same directory
@app.route('/style.css')
def style_css():
    """Serve the CSS file"""
    return send_from_directory('.', 'style.css')

@app.route('/script.js')
def script_js():
    """Serve the JavaScript file"""
    return send_from_directory('.', 'script.js')

if __name__ == '__main__':
    print("=" * 60)
    print("🎬 THE HOLY KEANU PHILOSOPHICAL AI IS STARTING UP 🎬")
    print("=" * 60)
    print(f"API Key configured: {'✓' if API_KEY != 'YOUR_API_KEY_HERE' else '✗'}")
    print(f"Keanu ready: {'✓' if keanu.configured else '✗'}")
    print("\nKeanu awaits your philosophical questions at: http://localhost:5000")
    print("Ask about life, existence, meaning, or any deep question...")
    print("Remember: Be excellent to each other! 🤙")
    print("=" * 60)
    app.run(host='0.0.0.0', port=10000)
    
    

