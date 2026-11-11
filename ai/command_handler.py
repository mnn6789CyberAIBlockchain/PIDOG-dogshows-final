"""
PiDog Final Project
AI Command Handler

Detects safe user commands and connects them
to approved PiDog actions and performances.
"""

from shows.demo_show import run_demo_show


def handle_command(question, dog):
    """
    Check the user's question for supported commands.

    Returns True if a command was executed.
    Returns False if normal AI conversation should continue.
    """

    command = question.lower().strip()


    # =============================================
    # DANCE / PERFORMANCE COMMAND
    # =============================================

    dance_commands = [
        "dance",
        "ok dance",
        "start dancing",
        "start the dance",
        "perform",
        "start performance",
        "start the performance"
    ]

    if command in dance_commands:

        print("\nPiDog Command Detected: DANCE")

        print("Starting Demo Performance...")

        run_demo_show(dog)

        return True


    # =============================================
    # SIT COMMAND
    # =============================================

    sit_commands = [
        "sit",
        "sit down"
    ]

    if command in sit_commands:

        print("\nPiDog Command Detected: SIT")

        dog.sit(speed=180)

        return True


    # =============================================
    # STAND COMMAND
    # =============================================

    stand_commands = [
        "stand",
        "stand up"
    ]

    if command in stand_commands:

        print("\nPiDog Command Detected: STAND")

        dog.stand(speed=180)

        return True


    # =============================================
    # WAG TAIL COMMAND
    # =============================================

    wag_commands = [
        "wag",
        "wag your tail",
        "wag tail"
    ]

    if command in wag_commands:

        print("\nPiDog Command Detected: WAG TAIL")

        dog.wag_tail(
            count=5,
            speed=190
        )

        return True


    # =============================================
    # NO COMMAND FOUND
    # =============================================

    return False