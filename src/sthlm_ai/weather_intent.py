# Import the function we wrote in llm_client.py
from sthlm_ai.llm_client import ask_structured

# This is the instruction we give to the LLM
SYSTEM = """
You are a classifier for a Stockholm weather assistant.
Return JSON with these exact keys:
- intent: one of ["current", "forecast", "history", "unknown"]
- location: string (default "Stockholm")
- days_ahead: integer or null
- confidence: float between 0 and 1
"""

# This function takes a user's question and returns a dictionary
def classify(text: str) -> dict:
    # Call the LLM and force it to answer in the format we described above
    return ask_structured(SYSTEM, text)

# This part only runs when we execute this file directly
if __name__ == "__main__":
    # Three example questions we want to test
    tests = [
        "Will it rain tomorrow in Stockholm?",
        "What was the temperature last week?",
        "Hello",
    ]
    # Loop through each test question
    for t in tests:
        # Print the question and the result from the LLM
        print(t, "->", classify(t))