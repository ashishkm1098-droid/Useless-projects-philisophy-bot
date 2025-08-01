import os
import google.generativeai as genai
import sys

# Instructions for the user:
# 1. Install the necessary library: pip install google-generativeai
# 2. Get your API key from the Google AI Studio.
# 3. Paste your API key directly below.

# --- PASTE YOUR API KEY HERE ---
# Replace "YOUR_API_KEY_HERE" with the actual key you received.
API_KEY = "AIzaSyCKrMXxF9T2uRtpjQlGLGbk0J-fZHIi7Ic"

# Configure the API with your key.
try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    print("An error occurred during API configuration.")
    print(f"Please double-check that you have pasted your API key correctly. Error details: {e}")
    sys.exit(1)

def get_philosophical_quote(question):
    """
    Sends a user question to the Gemini API and retrieves a cryptic,
    philosophical quote.
    """
    # Initialize the model with the correct model name
    model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

    # The prompt instructs the AI to act as a cryptic oracle,
    # ensuring the response is abstract and not a direct answer.
    prompt_text = f"""You are a philosophical AI. Respond to the following user question with a single, cryptic, and profound philosophical quote that you have made up. The quote should be abstract and not directly answer the user's question.

User question: "{question}"

AI Response (a cryptic philosophical quote):"""

    try:
        # Generate the content from the model
        response = model.generate_content(prompt_text)

        # Return the generated text
        if response.candidates:
            return response.text
        else:
            return "The oracle is silent. Try asking a different question."

    except Exception as e:
        return f"An error occurred while consulting the oracle: {e}"

def main():
    """
    The main function to run the command-line application.
    """
    print("--- The Oracle's Enigma ---")
    print("Ask a question, and the philosophical AI will provide a cryptic quote.")
    print("Type 'exit' or 'quit' to end the session.")
    print("-" * 27)

    while True:
        user_question = input("\nYour question: ")

        if user_question.lower() in ['exit', 'quit']:
            print("Session ended. Farewell.")
            break

        if not user_question.strip():
            print("Please enter a question.")
            continue

        print("Pondering...")
        quote = get_philosophical_quote(user_question)
        print(f"\nOracle's Reply: \"{quote}\"")

if __name__ == "__main__":
    main()
