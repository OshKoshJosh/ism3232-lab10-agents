# tests/test_my_assistant.py
# Author: Joshua Reddish

from my_assistant import GuitarAssistant
from my_tool import GuitarLookup


def make_assistant():
    """Create a fresh guitar assistant for each test."""
    guitars = {
        "Jazzmaster": {"price": 1299, "availability": "in stock"},
        "Telecaster": {"price": 799, "availability": "out of stock"},
    }
    tool = GuitarLookup(guitars)
    return GuitarAssistant("AmpBot", tool)


def test_guitar_lookup():
    bot = make_assistant()
    reply = bot.respond("How much is a Jazzmaster?")
    assert "$1299" in reply
    assert "in stock" in reply


def test_missing_guitar_name():
    bot = make_assistant()
    reply = bot.respond("What guitar should I buy?")
    assert "Which guitar model" in reply


def test_human_handoff():
    bot = make_assistant()
    reply = bot.respond("I need a refund")
    assert "human employee" in reply


def test_unknown_question():
    bot = make_assistant()
    reply = bot.respond("What is the weather?")
    assert "not sure" in reply


def test_conversation_history():
    bot = make_assistant()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"
