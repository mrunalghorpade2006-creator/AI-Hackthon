import os
from google import genai
from google.genai import types

from calculator import calculator
from weather import get_weather
from text_utility import text_utility
from wikipedia_tool import wikipedia_summary


client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


def calculate(operation: str, a: float, b: float) -> str:
    """Performs a mathematical calculation.

    Args:
        operation: add, subtract, multiply, or divide.
        a: First number.
        b: Second number.
    """
    return str(calculator(operation, a, b))


def weather(city: str) -> str:
    """Gets the current weather for a city.

    Args:
        city: Name of the city.
    """
    return get_weather(city)


def text_tool(text: str, operation: str) -> str:
    """Performs a text operation.

    Args:
        text: The text to process.
        operation: uppercase, lowercase, reverse, or length.
    """
    return str(text_utility(text, operation))


def wikipedia(topic: str) -> str:
    """Gets a short Wikipedia summary.

    Args:
        topic: Topic to search.
    """
    return wikipedia_summary(topic)


tools = [
    calculate,
    weather,
    text_tool,
    wikipedia
]


config = types.GenerateContentConfig(
    tools=tools
)


print("🤖 AI Multi-Tool Assistant")
print("Type 'exit' to stop.")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
        config=config
    )

    print("AI:", response.text)