"""
PiDog Final Project
Christmas Performance

Approximate Duration: 1 Minute

Features:
- Christmas music playing in the background
- PiDog choreography
- RGB light effects
- Automatic music stop after the performance
"""

import time
from audio.music_player import MusicPlayer


# =================================================
# SETTINGS
# =================================================

SHOW_DURATION = 60

MUSIC_FILE = "music/christmas_song.wav"


def pause(seconds):
    """Pause between choreography actions."""
    time.sleep(seconds)


# =================================================
# CHRISTMAS SHOW
# =================================================

def run_christmas_show(dog):

    print("\n" + "=" * 55)
    print("STARTING CHRISTMAS PERFORMANCE")
    print("=" * 55)

    # Create music player
    music = MusicPlayer()

    try:

        # =============================================
        # START MUSIC
        # =============================================

        print("\nStarting Christmas music...")

        music.play(MUSIC_FILE)

        show_start = time.time()


        # =============================================
        # OPENING
        # =============================================

        print("\nChristmas Opening")

        dog.set_light("red", bps=3)

        dog.stand(speed=180)
        pause(1)

        dog.wag_tail(count=4, speed=190)
        pause(1)


        # =============================================
        # DANCE LOOP
        # Continue dancing until approximately
        # 60 seconds have passed.
        # =============================================

        dance_round = 1

        while True:

            elapsed = time.time() - show_start

            if elapsed >= SHOW_DURATION:
                break

            print(
                f"\nChristmas Dance Round {dance_round}"
            )

            # -----------------------------------------
            # GREEN SECTION
            # -----------------------------------------

            dog.set_light("green", bps=4)

            dog.head_move(yaw=25, speed=190)
            dog.head_move(yaw=-25, speed=190)

            dog.turn_left(
                steps=1,
                speed=180
            )

            dog.turn_right(
                steps=1,
                speed=180
            )

            dog.wag_tail(
                count=3,
                speed=200
            )

            # -----------------------------------------
            # BLUE SECTION
            # -----------------------------------------

            dog.set_light("blue", bps=4)

            dog.forward(
                steps=1,
                speed=180
            )

            dog.backward(
                steps=1,
                speed=180
            )

            # -----------------------------------------
            # SPECIAL MOVE
            # -----------------------------------------

            dog.set_light("yellow", bps=5)

            dog.push_up(
                speed=180,
                repetitions=1
            )

            # -----------------------------------------
            # PERSONALITY MOVEMENT
            # -----------------------------------------

            dog.set_light("red", bps=5)

            dog.head_move(
                yaw=30,
                speed=200
            )

            dog.head_move(
                yaw=-30,
                speed=200
            )

            dog.wag_tail(
                count=4,
                speed=200
            )

            dance_round += 1


        # =============================================
        # FINALE
        # =============================================

        print("\nChristmas Finale!")

        dog.set_light("green", bps=5)

        dog.wag_tail(
            count=8,
            speed=200
        )

        dog.head_move(
            yaw=25,
            speed=190
        )

        dog.head_move(
            yaw=-25,
            speed=190
        )

        dog.head_move(
            yaw=0,
            speed=180
        )

        dog.sit(speed=180)


    finally:

        # =============================================
        # STOP MUSIC
        # =============================================

        music.stop()

        print(
            "\nChristmas Performance Complete!"
        )