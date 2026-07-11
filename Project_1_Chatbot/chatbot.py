"""
Project 1: Rule-Based AI Chatbot
Author: Alishba Yousaf
"""

def display_menu():
    """Display the list of available commands to the user."""
    print("\n--- Available Commands ---")
    print("- hello")
    print("- what is your name")
    print("- how are you")
    print("- project")
    print("- bye")
    print("--------------------------\n")

def run_chatbot():
    knowledge_base = {
        "hello": "Hi there! I am your AI assistant.",
        "what is your name": "I am a Rule-Based Chatbot created for DecodeLabs.",
        "how are you": "I am functioning perfectly!",
        "project": "This is Project 1, focusing on Python logic.",
        "bye": "Goodbye! Have a productive day."
    }

    print("--- DecodeLabs Assistant Initialized ---")
    display_menu() # Yahan hum user ko options dikha rahe hain

    while True:
        user_query = input("You: ").strip().lower()

        if user_query == 'exit':
            break
        
        # Agar user ka sawal dictionary mein hai to jawab milega, 
        # warna menu dubara dikha denge.
        if user_query in knowledge_base:
            print(f"Chatbot: {knowledge_base[user_query]}")
        else:
            print("Chatbot: I'm sorry, I don't know that one. Please try from the menu:")
            display_menu()

if __name__ == "__main__":
    run_chatbot()
