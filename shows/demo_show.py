"""
PiDog Final Project
Demo Performance

A short robotic performance using:
- Movement
- Head motion
- Tail movement
- RGB lights
"""


import time


def pause(seconds):
    time.sleep(seconds)


def run_demo_show(dog):

    print("\n" + "=" * 50)
    print("STARTING PIDOG DEMO PERFORMANCE")
    print("=" * 50)

    # =============================================
    # OPENING
    # =============================================

    print("\nOpening...")

    dog.set_light("blue", bps=2)

    dog.stand(speed=180)
    pause(1)

    dog.wag_tail(count=4, speed=190)
    pause(0.5)

    # =============================================
    # WALKING SECTION
    # =============================================

    print("Walking performance...")

    dog.set_light("green", bps=3)

    dog.forward(steps=2, speed=180)
    pause(0.5)

    dog.turn_left(steps=1, speed=180)
    pause(0.5)

    dog.forward(steps=2, speed=180)
    pause(0.5)

    # =============================================
    # HEAD DANCE
    # =============================================

    print("Head movement performance...")

    dog.set_light("red", bps=4)

    for _ in range(3):

        dog.head_move(yaw=30, speed=190)
        pause(0.3)

        dog.head_move(yaw=-30, speed=190)
        pause(0.3)

    dog.head_move(yaw=0, pitch=0, speed=180)

    # =============================================
    # BODY ACTION
    # =============================================

    print("Body action...")

    dog.set_light("yellow", bps=3)

    dog.stretch(speed=180)
    pause(1)

    dog.stand(speed=180)
    pause(0.5)

    # =============================================
    # FINALE
    # =============================================

    print("Finale...")

    dog.set_light("green", bps=5)

    dog.wag_tail(count=8, speed=200)

    dog.head_move(yaw=25, speed=190)
    pause(0.4)

    dog.head_move(yaw=-25, speed=190)
    pause(0.4)

    dog.head_move(yaw=0, pitch=0, speed=180)

    dog.sit(speed=180)

    print("\nDemo Performance Complete!")