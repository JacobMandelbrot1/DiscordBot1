import openai
from cs50 import SQL


db = SQL("sqlite:///feedback.db")
openai.api_key = "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"

def handle_responses(message) -> str:
    p_message = message.lower()
    response = ""

    if(p_message == "hi"):
        response = ("No memes in general")
    return response
