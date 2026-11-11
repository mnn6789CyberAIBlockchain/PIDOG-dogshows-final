"""
PiDog Final Project
AI Reaction System

Controls PiDog's physical reactions during
AI conversations.
"""


def thinking_reaction(dog):

    print("\nPiDog is thinking...")

    dog.set_light("blue", bps=2)

    dog.head_move(
        yaw=15,
        pitch=10,
        speed=160
    )

    dog.head_move(
        yaw=-15,
        pitch=10,
        speed=160
    )

    dog.head_move(
        yaw=0,
        pitch=0,
        speed=160
    )


def happy_reaction(dog):

    print("\nPiDog is happy!")

    dog.set_light("green", bps=3)

    dog.wag_tail(
        count=4,
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


def listening_reaction(dog):

    print("\nPiDog is listening...")

    dog.set_light("yellow", bps=2)

    dog.head_move(
        pitch=15,
        speed=150
    )