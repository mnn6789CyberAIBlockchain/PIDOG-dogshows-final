"""
PiDog Final Project
Introduction Performance

PiDog introduces itself using:
- Voice narration
- Safe movement
- Head actions
- Tail wagging
- RGB lights
"""

import time


def pause(seconds):
    """Pause between performance actions."""
    time.sleep(seconds)


def speak(dog, text):
    """Speak and pause briefly for a stable performance."""
    dog.speak(text)
    pause(0.5)


def run_introduction_show(dog):

    print("\n" + "=" * 55)
    print("STARTING PIDOG INTRODUCTION PERFORMANCE")
    print("=" * 55)

    # =================================================
    # SECTION 1 - GRAND ENTRANCE
    # =================================================

    print("\n[1/5] GRAND ENTRANCE")

    dog.set_light("blue", bps=2)

    dog.stand(speed=120)
    pause(2)

    speak(
        dog,
        "Hello everyone! My name is PiDog."
    )

    # Safer: only one forward step
    dog.forward(steps=1, speed=110)
    pause(2)

    dog.wag_tail(count=3, speed=140)
    pause(1)

    # =================================================
    # SECTION 2 - GREETING THE AUDIENCE
    # =================================================

    print("\n[2/5] GREETING THE AUDIENCE")

    dog.set_light("green", bps=2)

    speak(
        dog,
        "I am a friendly AI-powered robotic dog "
        "created as part of a university final project."
    )

    # Slower head movements are much safer than fast body turns
    dog.head_move(yaw=25, speed=120)
    pause(1)

    dog.head_move(yaw=-25, speed=120)
    pause(1)

    dog.head_move(yaw=0, speed=120)
    pause(1)

    dog.wag_tail(count=4, speed=140)
    pause(1)

    # =================================================
    # SECTION 3 - SHOWING MOVEMENT ABILITIES
    # =================================================

    print("\n[3/5] MOVEMENT DEMONSTRATION")

    dog.set_light("yellow", bps=2)

    speak(
        dog,
        "I can walk, turn, move my head, "
        "wag my tail, and perform interactive shows."
    )

    # SAFER MOVEMENT DEMONSTRATION
    dog.forward(steps=1, speed=110)
    pause(2)

    dog.stand(speed=110)
    pause(2)

    # Head movement instead of risky fast turning
    dog.head_move(yaw=30, speed=120)
    pause(1)

    dog.head_move(yaw=-30, speed=120)
    pause(1)

    dog.head_move(yaw=0, speed=120)
    pause(2)

    # =================================================
    # SECTION 4 - AI PERSONALITY
    # =================================================

    print("\n[4/5] AI PERSONALITY")

    dog.set_light("purple", bps=3)

    speak(
        dog,
        "I also have an AI brain powered by Ollama. "
        "You can ask me questions, and I can respond."
    )

    for _ in range(2):

        dog.head_move(yaw=20, speed=120)
        pause(0.7)

        dog.head_move(yaw=-20, speed=120)
        pause(0.7)

    dog.head_move(yaw=0, speed=120)
    pause(1)

    dog.wag_tail(count=5, speed=150)
    pause(1)

    # =================================================
    # SECTION 5 - FINALE
    # =================================================

    print("\n[5/5] INTRODUCTION FINALE")

    dog.set_light("red", bps=3)

    speak(
        dog,
        "Thank you for watching my performance!"
    )

    pause(1)

    # Keep finale simple and stable
    dog.stand(speed=110)
    pause(1)

    dog.set_light("green", bps=3)

    dog.wag_tail(count=6, speed=150)
    pause(1)

    speak(
        dog,
        "I am PiDog, your AI-powered robotic performer. "
        "Thank you!"
    )

    dog.sit(speed=110)

    print("\nPiDog Introduction Performance Complete!")