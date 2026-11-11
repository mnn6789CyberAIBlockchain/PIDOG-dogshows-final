"""
PiDog Final Project
Interactive Human-PiDog Show

This performance demonstrates:

1. PiDog gets the audience's attention after a clap.
2. The interviewer says: "PiDog, come here!"
3. PiDog walks toward the interviewer.
4. The interviewer says: "PiDog, high five!"
5. PiDog performs a right paw high five.
6. PiDog performs a left paw high five.
7. PiDog celebrates and transitions to AI Q&A.

The sensor-based clap detection will be tested and
connected to the real PiDog hardware on the Raspberry Pi.
"""


import time


# =================================================
# ATTENTION / CLAP REACTION
# =================================================

def attention_reaction(dog):

    print("\n" + "=" * 55)
    print("INTERACTIVE MODE: ATTENTION DETECTED")
    print("=" * 55)

    print("\nPiDog noticed the audience!")

    dog.set_light("yellow", bps=2)

    # Look toward the audience.
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

    # Friendly reaction.
    dog.wag_tail(
        count=2,
        speed=180
    )

    time.sleep(1)


# =================================================
# COME HERE / APPROACH
# =================================================

def come_here(dog):

    print("\nInterviewer: PiDog, come here!")

    print("\nPiDog is approaching...")

    dog.set_light("blue", bps=2)

    # Make sure PiDog is standing before walking.
    dog.stand(speed=160)

    time.sleep(1)

    # Controlled approach.
    #
    # IMPORTANT:
    # We will tune the number of steps on the real PiDog
    # depending on the actual distance to the interviewer.
    dog.forward(
        steps=2,
        speed=150
    )

    time.sleep(1)

    dog.forward(
        steps=1,
        speed=130
    )

    # Stop safely.
    dog.stop()

    print("\nPiDog has reached the interviewer!")

    dog.set_light("green", bps=2)

    dog.wag_tail(
        count=2,
        speed=170
    )

    time.sleep(1)


# =================================================
# HIGH FIVE
# =================================================

def high_five(dog):

    print("\nInterviewer: PiDog, high five!")

    print("\nPiDog is ready for a high five!")

    dog.set_light("purple", bps=2)

    time.sleep(1)

    # -------------------------------------------------
    # RIGHT PAW HIGH FIVE
    # -------------------------------------------------

    print("\nRIGHT PAW HIGH FIVE!")

    # Temporary choreography movement.
    #
    # The exact individual-leg API will be verified
    # on the real PiDog before the final demonstration.
    dog.head_move(
        yaw=15,
        pitch=15,
        speed=150
    )

    dog.stretch(speed=140)

    time.sleep(1)

    print("High five!")

    time.sleep(1)

    dog.stand(speed=150)

    time.sleep(1)

    # -------------------------------------------------
    # LEFT PAW HIGH FIVE
    # -------------------------------------------------

    print("\nLEFT PAW HIGH FIVE!")

    dog.head_move(
        yaw=-15,
        pitch=15,
        speed=150
    )

    dog.stretch(speed=140)

    time.sleep(1)

    print("High five!")

    time.sleep(1)

    dog.stand(speed=150)

    time.sleep(1)

    # -------------------------------------------------
    # HAPPY CELEBRATION
    # -------------------------------------------------

    print("\nPiDog is happy!")

    dog.set_light("green", bps=3)

    dog.wag_tail(
        count=4,
        speed=190
    )

    dog.head_move(
        yaw=20,
        speed=170
    )

    dog.head_move(
        yaw=-20,
        speed=170
    )

    dog.head_move(
        yaw=0,
        speed=170
    )

    time.sleep(1)


# =================================================
# COMPLETE INTERACTIVE SHOW
# =================================================

def run_interactive_show(dog):

    print("\n" + "=" * 60)
    print("STARTING PIDOG INTERACTIVE PERFORMANCE")
    print("=" * 60)

    # ---------------------------------------------
    # STEP 1 — CLAP / ATTENTION
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

    print("\n" + "=" * 60)
    print("INTERACTIVE PERFORMANCE COMPLETE!")
    print("=" * 60)