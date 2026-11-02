# two_bots.py
# Author: Joshua Reddish

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

# Create tools that both chatbots will share.
order_tool = OrderLookup({"A100": "shipped", "A101": "processing"})
stock_tool = StockLookup({"rain jacket": 12, "backpack": 8})

# Create two different chatbot objects from the same class.
sunny = SupportChatbot(
    "Sunny",
    "You are cheerful and brief.",
    order_tool,
    stock_tool,
)

river = SupportChatbot(
    "River",
    "You are formal and detailed.",
    order_tool,
    stock_tool,
)

# Give Sunny two messages and River one.
print("Sunny:", sunny.respond("hello"))
print("Sunny:", sunny.respond("Where is order A100?"))
print("River:", river.respond("hello"))

# Show that each chatbot has its own history and instructions.
print("Sunny history length:", len(sunny.history))
print("River history length:", len(river.history))
print("Sunny instructions:", sunny.instructions)
print("River instructions:", river.instructions)
