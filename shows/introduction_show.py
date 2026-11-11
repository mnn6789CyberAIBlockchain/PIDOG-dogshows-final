"""
PiDog Final Project
Introduction Performance

Approximate Duration: 1 Minute

PiDog introduces itself using:
- Movement
- Head actions
- Tail wagging
- RGB lights
"""

import time


def pause(seconds):
    """Pause between performance actions."""
    time.sleep(seconds)


def run_introduction_show(dog):

    print("\n" + "=" * 55)
    print("STARTING PIDOG INTRODUCTION PERFORMANCE")
    print("=" * 55)

    # =================================================
    # SECTION 1 - GRAND ENTRANCE
    # =================================================

    print("\n[1/5] GRAND ENTRANCE")

    dog.set_light("blue", bps=2)

    dog.stand(speed=180)
    pause(1)

    dog.forward(steps=2, speed=180)
    pause(1)

    dog.turn_left(steps=1, speed=180)
    pause(1)

    dog.wag_tail(count=4, speed=190)
    pause(1)

    # =================================================
    # SECTION 2 - GREETING THE AUDIENCE
    # =================================================

    print("\n[2/5] GREETING THE AUDIENCE")

    dog.set_light("green", bps=3)

    dog.head_move(yaw=30, speed=180)
    pause(1)

    dog.head_move(yaw=-30, speed=180)
    pause(1)

    dog.head_move(yaw=0, speed=180)
    pause(1)

    dog.wag_tail(count=5, speed=190)
    pause(1)

    # =================================================
    # SECTION 3 - SHOWING MOVEMENT ABILITIES
    # =================================================

    print("\n[3/5] MOVEMENT DEMONSTRATION")

    dog.set_light("yellow", bps=3)

    dog.forward(steps=2, speed=180)
    pause(1)

    dog.turn_right(steps=1, speed=180)
    pause(1)

    dog.backward(steps=1, speed=180)
    pause(1)

    dog.stand(speed=180)
    pause(1)

    # =================================================
    # SECTION 4 - ROBOT PERSONALITY
    # =================================================

    print("\n[4/5] ROBOT PERSONALITY")

    dog.set_light("purple", bps=4)

    for _ in range(2):

        dog.head_move(yaw=25, speed=190)
        pause(0.5)

        dog.head_move(yaw=-25, speed=190)
        pause(0.5)

    dog.head_move(yaw=0, speed=180)

    dog.wag_tail(count=6, speed=200)
    pause(1)

    # =================================================
    # SECTION 5 - FINALE
    # =================================================

    print("\n[5/5] INTRODUCTION FINALE")

    dog.set_light("red", bps=4)

    dog.stretch(speed=180)
    pause(1)

    dog.stand(speed=180)
    pause(1)

    dog.set_light("green", bps=5)

    dog.wag_tail(count=8, speed=200)

    dog.sit(speed=180)

    print("\nPiDog Introduction Performance Complete!")