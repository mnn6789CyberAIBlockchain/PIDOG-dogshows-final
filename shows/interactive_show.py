"""
PiDog Final Project
Interactive Human-PiDog Show

This performance demonstrates:

1. PiDog gets the audience's attention.
2. The interviewer says: "PiDog, come here!"
3. PiDog walks toward the interviewer.
4. The interviewer says: "PiDog, high five!"
5. PiDog performs the high-five demonstration.
6. PiDog celebrates.
7. PiDog answers questions using local Ollama AI.
"""

import time

from ai.ollama_brain import ask_pidog


# =================================================
# HELPER: PIDOG SPEAKING
# =================================================

def speak(dog, text):
    """Make PiDog speak and briefly pause."""

    print(f"\n🔊 PiDog: {text}")

    dog.speak(text)

    # Small pause so actions do not immediately interrupt speech
    time.sleep(0.5)


# =================================================
# ATTENTION / CLAP REACTION
# =================================================

def attention_reaction(dog):

    print("\n" + "=" * 55)
    print("INTERACTIVE MODE: ATTENTION DETECTED")
    print("=" * 55)

    dog.set_light("yellow", bps=2)

    speak(
        dog,
        "Hello everyone! I noticed you."
    )

    # Look toward the audience
    dog.head_move(
        yaw=25,
        pitch=10,
        speed=150
    )

    time.sleep(0.5)

    dog.head_move(
        yaw=-25,
        pitch=10,
        speed=150
    )

    time.sleep(0.5)

    dog.head_move(
        yaw=0,
        pitch=0,
        speed=150
    )

    dog.wag_tail(
        count=2,
        speed=160
    )

    time.sleep(1)


# =================================================
# COME HERE / APPROACH
# =================================================

def come_here(dog):

    print("\nInterviewer: PiDog, come here!")

    dog.set_light("blue", bps=2)

    speak(
        dog,
        "Okay! I am coming."
    )

    # Make sure PiDog is standing before walking
    dog.stand(speed=140)

    time.sleep(1)

    # Controlled approach
    dog.forward(
        steps=1,
        speed=120
    )

    time.sleep(1)

    # Stop safely
    dog.stop()

    print("\nPiDog has reached the interviewer!")

    dog.set_light("green", bps=2)

    speak(
        dog,
        "I am here!"
    )

    dog.wag_tail(
        count=2,
        speed=160
    )

    time.sleep(1)


# =================================================
# HIGH FIVE
# =================================================

def high_five(dog):

    print("\nInterviewer: PiDog, high five!")

    dog.set_light("purple", bps=2)

    speak(
        dog,
        "High five!"
    )

    time.sleep(1)

    # -------------------------------------------------
    # RIGHT PAW DEMONSTRATION
    # -------------------------------------------------

    print("\nRIGHT PAW HIGH FIVE!")

    dog.head_move(
        yaw=15,
        pitch=10,
        speed=140
    )

    # Use controlled movement
    dog.stretch(speed=120)

    time.sleep(1)

    speak(
        dog,
        "Right paw!"
    )

    time.sleep(1)

    dog.stand(speed=130)

    time.sleep(1)

    # -------------------------------------------------
    # LEFT PAW DEMONSTRATION
    # -------------------------------------------------

    print("\nLEFT PAW HIGH FIVE!")

    dog.head_move(
        yaw=-15,
        pitch=10,
        speed=140
    )

    dog.stretch(speed=120)

    time.sleep(1)

    speak(
        dog,
        "And left paw!"
    )

    time.sleep(1)

    dog.stand(speed=130)

    time.sleep(1)

    # -------------------------------------------------
    # HAPPY CELEBRATION
    # -------------------------------------------------

    print("\nPiDog is happy!")

    dog.set_light("green", bps=3)

    speak(
        dog,
        "That was fun!"
    )

    dog.wag_tail(
        count=3,
        speed=160
    )

    dog.head_move(
        yaw=15,
        speed=150
    )

    dog.head_move(
        yaw=-15,
        speed=150
    )

    dog.head_move(
        yaw=0,
        speed=150
    )

    time.sleep(1)


# =================================================
# AI QUESTION AND ANSWER
# =================================================

def interactive_ai_questions(dog):

    print("\n" + "=" * 60)
    print("PIDOG INTERACTIVE AI QUESTION AND ANSWER")
    print("=" * 60)

    dog.set_light("yellow", bps=2)

    speak(
        dog,
        "Now you can ask me questions. Type exit when you are finished."
    )

    while True:

        print("\nPiDog is listening...")
        dog.set_light("yellow", bps=2)

        question = input("\nYou: ").strip()

        # Exit Q&A
        if question.lower() in ["exit", "quit", "bye"]:

            speak(
                dog,
                "Thank you for talking with me. Goodbye!"
            )

            break

        # Ignore empty questions
        if not question:
            continue

        print("\nPiDog is thinking...")

        dog.set_light("blue", bps=2)

        # Ask local Ollama AI
        answer = ask_pidog(question)

        # Display answer
        print(f"\nPiDog: {answer}")

        # Speak answer through PiDog speaker
        dog.speak(answer)

        # Happy reaction
        dog.set_light("green", bps=2)

        dog.wag_tail(
            count=1,
            speed=150
        )

        time.sleep(0.5)


# =================================================
# COMPLETE INTERACTIVE SHOW
# =================================================

def run_interactive_show(dog):

    print("\n" + "=" * 60)
    print("STARTING PIDOG INTERACTIVE PERFORMANCE")
    print("=" * 60)

    # ---------------------------------------------
    # STEP 1 — ATTENTION
    # ---------------------------------------------

    input(
        "\nPress ENTER to simulate the audience clap..."
    )

    attention_reaction(dog)

    # ---------------------------------------------
    # STEP 2 — COME HERE
    # ---------------------------------------------

    input(
        "\nPress ENTER when you say: "
        "'PiDog, come here!'..."
    )

    come_here(dog)

    # ---------------------------------------------
    # STEP 3 — HIGH FIVE
    # ---------------------------------------------

    input(
        "\nPress ENTER when you say: "
        "'PiDog, high five!'..."
    )

    high_five(dog)

    # ---------------------------------------------
    # STEP 4 — AI QUESTIONS
    # ---------------------------------------------

    input(
        "\nPress ENTER to begin PiDog AI Question and Answer..."
    )

    interactive_ai_questions(dog)

    print("\n" + "=" * 60)
    print("INTERACTIVE PERFORMANCE COMPLETE!")
    print("=" * 60)