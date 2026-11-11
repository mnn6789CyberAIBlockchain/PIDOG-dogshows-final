"""
PiDog Final Project
Christmas Performance

Timing:
- Christmas song: 62 seconds
- Post-song reset: approximately 1.5 seconds
"""

import os
import time

from audio.music_player import MusicPlayer


# =================================================
# SETTINGS
# =================================================

SONG_DURATION = 62.0
RESET_TIME = 1.5

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MUSIC_FILE = os.path.join(
    BASE_DIR,
    "music",
    "christmas_song.wav"
)


# =================================================
# HELPERS
# =================================================

def pause(seconds):
    time.sleep(seconds)


def return_to_home(dog):
    """
    Return PiDog to a stable presentation posture
    after the music finishes.
    """

    print("\nReturning PiDog to home posture...")

    dog.set_light("green", bps=2)

    dog.head_move(
        yaw=0,
        roll=0,
        pitch=0,
        speed=180
    )

    dog.stand(speed=180)

    pause(RESET_TIME)


# =================================================
# CHRISTMAS SHOW
# =================================================

def run_christmas_show(dog):

    print("\n" + "=" * 55)
    print("STARTING CHRISTMAS PERFORMANCE")
    print("=" * 55)

    music = MusicPlayer()

    start_time = time.monotonic()

    try:

        # =============================================
        # START MUSIC
        # =============================================

        print("\nStarting Christmas music...")

        music.play(MUSIC_FILE)

        # =============================================
        # OPENING
        # =============================================

        print("\nChristmas Opening")

        dog.set_light(
            "red",
            bps=3
        )

        dog.stand(
            speed=180
        )

        dog.wag_tail(
            count=4,
            speed=190
        )

        # =============================================
        # FULL SONG CHOREOGRAPHY
        # =============================================

        dance_round = 1

        while True:

            elapsed = time.monotonic() - start_time

            if elapsed >= SONG_DURATION:
                break

            print(
                f"\nChristmas Dance Round {dance_round}"
            )

            # -----------------------------------------
            # GREEN SECTION
            # -----------------------------------------

            dog.set_light(
                "green",
                bps=4
            )

            dog.head_move(
                yaw=25,
                speed=190
            )

            dog.head_move(
                yaw=-25,
                speed=190
            )

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

            dog.set_light(
                "blue",
                bps=4
            )

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

            dog.set_light(
                "yellow",
                bps=5
            )

            dog.push_up(
                speed=180,
                repetitions=1
            )

            # -----------------------------------------
            # PERSONALITY
            # -----------------------------------------

            dog.set_light(
                "red",
                bps=5
            )

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
        # SONG FINISHED
        # =============================================

        print("\nChristmas song finished.")

        music.stop()

        # =============================================
        # RESET POSTURE
        # =============================================

        return_to_home(dog)

        elapsed = time.monotonic() - start_time

        print(
            f"\nChristmas Performance Complete!"
        )

        print(
            f"Total performance time: {elapsed:.1f} seconds"
        )

    finally:

        music.stop()