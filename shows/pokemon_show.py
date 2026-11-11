"""
PiDog Final Project
Pokemon Performance

Timing:
- Pokemon song: 58 seconds
- Post-song reset: approximately 1.5 seconds
"""

import os
import time

from audio.music_player import MusicPlayer


# =================================================
# SETTINGS
# =================================================

SONG_DURATION = 58.0
RESET_TIME = 1.5

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MUSIC_FILE = os.path.join(
    BASE_DIR,
    "music",
    "pokemon_song.wav"
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

    dog.set_light(
        "green",
        bps=2
    )

    dog.head_move(
        yaw=0,
        roll=0,
        pitch=0,
        speed=180
    )

    dog.stand(
        speed=180
    )

    pause(RESET_TIME)


# =================================================
# POKEMON SHOW
# =================================================

def run_pokemon_show(dog):

    print("\n" + "=" * 55)
    print("STARTING POKEMON PERFORMANCE")
    print("=" * 55)

    music = MusicPlayer()

    start_time = time.monotonic()

    try:

        # =============================================
        # START MUSIC
        # =============================================

        print("\nStarting Pokemon music...")

        music.play(MUSIC_FILE)

        # =============================================
        # OPENING
        # =============================================

        print("\nPokemon Opening")

        dog.set_light(
            "yellow",
            bps=4
        )

        dog.stand(
            speed=190
        )

        dog.head_move(
            yaw=30,
            speed=190
        )

        dog.head_move(
            yaw=-30,
            speed=190
        )

        dog.head_move(
            yaw=0,
            speed=190
        )

        dog.wag_tail(
            count=4,
            speed=200
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
                f"\nPokemon Dance Round {dance_round}"
            )

            # -----------------------------------------
            # MOVEMENT
            # -----------------------------------------

            dog.set_light(
                "blue",
                bps=5
            )

            dog.forward(
                steps=1,
                speed=190
            )

            dog.turn_left(
                steps=1,
                speed=190
            )

            dog.backward(
                steps=1,
                speed=190
            )

            dog.turn_right(
                steps=1,
                speed=190
            )

            # -----------------------------------------
            # HEAD RHYTHM
            # -----------------------------------------

            dog.set_light(
                "red",
                bps=5
            )

            dog.head_move(
                yaw=35,
                speed=200
            )

            dog.head_move(
                yaw=-35,
                speed=200
            )

            dog.head_move(
                yaw=0,
                speed=200
            )

            # -----------------------------------------
            # PUSH-UP
            # -----------------------------------------

            dog.set_light(
                "yellow",
                bps=6
            )

            dog.push_up(
                speed=190,
                repetitions=1
            )

            # -----------------------------------------
            # ENERGY
            # -----------------------------------------

            dog.set_light(
                "green",
                bps=6
            )

            dog.wag_tail(
                count=5,
                speed=200
            )

            dance_round += 1

        # =============================================
        # SONG FINISHED
        # =============================================

        print("\nPokemon song finished.")

        music.stop()

        # =============================================
        # RESET POSTURE
        # =============================================

        return_to_home(dog)

        elapsed = time.monotonic() - start_time

        print(
            f"\nPokemon Performance Complete!"
        )

        print(
            f"Total performance time: {elapsed:.1f} seconds"
        )

    finally:

        music.stop()