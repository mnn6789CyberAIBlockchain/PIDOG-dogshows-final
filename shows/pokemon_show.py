"""
PiDog Final Project
Pokemon Performance

Approximate Duration: 1 Minute

Features:
- Pokemon music playing in the background
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

MUSIC_FILE = "music/pokemon_song.wav"


def pause(seconds):
    """Pause between choreography actions."""
    time.sleep(seconds)


# =================================================
# POKEMON SHOW
# =================================================

def run_pokemon_show(dog):

    print("\n" + "=" * 55)
    print("STARTING POKEMON PERFORMANCE")
    print("=" * 55)

    # Create music player
    music = MusicPlayer()

    try:

        # =============================================
        # START MUSIC
        # =============================================

        print("\nStarting Pokemon music...")

        music.play(MUSIC_FILE)

        show_start = time.time()


        # =============================================
        # OPENING
        # =============================================

        print("\nPokemon Opening")

        dog.set_light("yellow", bps=4)

        dog.stand(speed=190)
        pause(1)

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
        # MAIN DANCE LOOP
        # =============================================

        dance_round = 1

        while True:

            elapsed = time.time() - show_start

            if elapsed >= SHOW_DURATION:
                break

            print(
                f"\nPokemon Dance Round {dance_round}"
            )

            # -----------------------------------------
            # BLUE SECTION
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
            # PUSH-UP SPECIAL MOVE
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
            # TAIL / ENERGY MOVE
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
        # FINALE
        # =============================================

        print("\nPokemon Finale!")

        dog.set_light(
            "yellow",
            bps=6
        )

        dog.stretch(
            speed=190
        )

        pause(0.5)

        dog.stand(
            speed=190
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

        dog.wag_tail(
            count=10,
            speed=200
        )

        dog.set_light(
            "green",
            bps=5
        )

        dog.sit(
            speed=190
        )


    finally:

        # =============================================
        # STOP MUSIC
        # =============================================

        music.stop()

        print(
            "\nPokemon Performance Complete!"
        )