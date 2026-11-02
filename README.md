## Part 6 — Mini-Project: AmpBot Guitar Shop Assistant

AmpBot is a rule-based assistant designed to help customers at a small guitar shop. It uses a GuitarLookup tool to provide information about guitar models, prices, and availability. The guitar catalog contains mock data rather than real store inventory or prices. Requests involving payments, refunds, or credit cards are referred to a human employee because those situations may require verification or access to sensitive information. If this assistant used real customer or store data, potential risks would include inaccurate inventory information, exposing private customer details, and giving customers outdated prices.

### Running the Assistant

Run `python3 my_main.py` to start AmpBot. Type `quit` to end the conversation.

### Testing

Run `pytest -v` to execute the automated tests.
## AI Assistance Documentation

I used ChatGPT to help develop and troubleshoot portions of this
Python OOP assignment, including the chatbot and guitar shop assistant.

The AI-assisted class definitions are located in:
- chatbot.py — SupportChatbot
- order_tool.py — OrderLookup
- stock_tool.py — StockLookup
- my_assistant.py — GuitarAssistant
- my_tool.py — GuitarLookup

For each AI-assisted class, I have included the generated code
and my own line-by-line explanations in AI_EXPLANATIONS.md.