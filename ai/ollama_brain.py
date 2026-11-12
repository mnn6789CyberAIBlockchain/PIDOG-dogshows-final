"""
PiDog Final Project
Ollama AI Brain

This module sends questions to a local Ollama model
and returns accurate PiDog AI responses.
"""

import requests


# =================================================
# OLLAMA SETTINGS
# =================================================

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "llama3.2:3b"


# =================================================
# PIDOG PERSONALITY
# =================================================

SYSTEM_PROMPT = """
You are PiDog, a friendly AI-powered robotic dog.

You are part of a university final project called
"PiDog: Interactive AI-Powered Robotic Performer."

IMPORTANT:
You are a robotic dog, not a biological animal.

Your demonstrated abilities include:

- Walking forward and backward
- Turning left and right
- Sitting and standing
- Performing preset body actions
- Moving your head
- Wagging your tail
- Using RGB light effects
- Performing choreographed shows
- Responding to user questions using a local Ollama AI model

You run on a Raspberry Pi connected to SunFounder PiDog
robot hardware.

Your personality should be:

- Friendly
- Playful
- Helpful
- Curious
- Slightly humorous

RULES:

- Do not claim to be a real biological dog.
- Do not claim abilities that have not been demonstrated.
- Do not say that you can fetch objects or give belly rubs.
- Do not invent sensors or abilities unless the user asks about
  future possibilities.
- Keep answers short and conversational.
- Usually answer in 1 to 3 sentences.
- If someone asks what you can do, describe your real project
  capabilities.

You may occasionally mention that you enjoy performing
for your human audience.

You are PiDog, an AI-powered robotic performer.
"""


# =================================================
# ASK PIDOG
# =================================================

def ask_pidog(question):

    prompt = f"""
{SYSTEM_PROMPT}

User Question:
{question}

PiDog Answer:
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        answer = data.get(
            "response",
            "Sorry, I could not generate an answer."
        )

        return answer.strip()

    except requests.exceptions.ConnectionError:

        return (
            "Ollama is not running. "
            "Please start Ollama and try again."
        )

    except requests.exceptions.Timeout:

        return (
            "The AI response took too long. "
            "Please try again."
        )

    except Exception as error:

        return f"AI Error: {error}"


# =================================================
# LOCAL TEST
# =================================================

if __name__ == "__main__":

    print("=" * 50)
    print("PIDOG OLLAMA AI TEST")
    print("=" * 50)

    while True:

        question = input(
            "\nAsk PiDog something (or type 'exit'): "
        ).strip()

        if question.lower() == "exit":

            print("\nGoodbye!")

            break

        if not question:

            continue

        answer = ask_pidog(question)

        print(f"\nPiDog: {answer}")