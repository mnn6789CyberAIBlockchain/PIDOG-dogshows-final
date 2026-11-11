"""
PiDog Final Project
Final Live AI Q&A

Final section of the complete presentation.
"""

import time

from ai.ollama_brain import ask_pidog
from ai.pidog_reactions import (
    listening_reaction,
    thinking_reaction,
    happy_reaction
)


def run_final_qa(dog):

    print("\n" + "=" * 60)
    print("FINAL LIVE AI Q&A")
    print("=" * 60)

    print("\nThe audience can now ask PiDog questions.")
    print("Type 'exit' to finish the final presentation.")

    start_time = time.time()
    duration = 60

    while True:

        elapsed = time.time() - start_time
        remaining = duration - elapsed

        if remaining <= 0:

            print("\nQ&A time is complete!")

            break

        print(
            f"\nQ&A time remaining: {int(remaining)} seconds"
        )

        listening_reaction(dog)

        question = input("\nAudience: ").strip()

        if question.lower() == "exit":

            print("\nEnding Q&A...")

            break

        if not question:

            continue

        thinking_reaction(dog)

        answer = ask_pidog(question)

        print(f"\nPiDog: {answer}")

        happy_reaction(dog)


    # Final goodbye reaction

    print("\nThank you for watching PiDog!")

    dog.set_light("green", bps=2)

    dog.wag_tail(
        count=6,
        speed=190
    )

    dog.head_move(
        yaw=20,
        speed=180
    )

    dog.head_move(
        yaw=-20,
        speed=180
    )

    dog.head_move(
        yaw=0,
        speed=180
    )

    dog.sit(speed=180)

    print("\nFINAL PRESENTATION COMPLETE!")