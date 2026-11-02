# my_main.py
# Author: Joshua Reddish

from my_assistant import GuitarAssistant
from my_tool import GuitarLookup

# Create a mock guitar catalog.
guitars = {
    "Jazzmaster": {"price": 1299, "availability": "in stock"},
    "Stratocaster": {"price": 899, "availability": "in stock"},
    "Telecaster": {"price": 799, "availability": "out of stock"},
    "Mustang": {"price": 749, "availability": "in stock"},
}

# Create the lookup tool and assistant.
guitar_tool = GuitarLookup(guitars)
bot = GuitarAssistant("AmpBot", guitar_tool)

print("Welcome to the guitar shop!")
print("Ask about a guitar model, or type quit to exit.")

# Keep chatting until the customer types quit.
while True:
    user_message = input("You: ")

    if user_message.lower() == "quit":
        break

    print(f"{bot.name}: {bot.respond(user_message)}")

print(f"Conversation history: {len(bot.history)} messages")
