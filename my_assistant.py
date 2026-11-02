# my_assistant.py
# Author: Joshua Reddish


class GuitarAssistant:
    """A rule-based assistant for a small guitar shop."""

    def __init__(self, name, guitar_tool):
        """Store the assistant's name, lookup tool, and history."""
        self.name = name
        self.guitar_tool = guitar_tool
        self.history = []

    def respond(self, user_message):
        """Record the conversation and return an appropriate reply."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a response using simple keyword rules."""
        text = user_message.lower()

        if any(word in text for word in ["payment", "refund", "card"]):
            return "I'll connect you with a human employee for that request."

        if "hello" in text or "hi" == text:
            return f"Hello! I'm {self.name}. I can help you find a guitar."

        guitar = self.guitar_tool.find_guitar(user_message)

        if guitar is not None:
            details = self.guitar_tool.get_details(guitar)
            return (
                f"The {guitar} costs ${details['price']} "
                f"and availability is {details['availability']}."
            )

        if "guitar" in text or "price" in text:
            return "Which guitar model would you like me to check?"

        return "I'm not sure about that. Please ask a store employee for help."
