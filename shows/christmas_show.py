"""
PiDog Final Project
Christmas Performance - Safe Version

Designed for improved stability:

- No walking
- No turning
- Slow movements
- Frequent recovery pauses
- Lie-down reset positions
- Head movements
- Tail wagging
- Controlled push-ups
- High-five moments
- RGB lights
- PiDog voice

Christmas song: approximately 62 seconds
"""

import os
import time

from audio.music_player import MusicPlayer


# =================================================
# SETTINGS
# =================================================

SONG_DURATION = 62.0
RESET_TIME = 1.5

# Safer movement speeds
HEAD_SPEED = 105
TAIL_SPEED = 120
BODY_SPEED = 100
PUSHUP_SPEED = 100
HIGH_FIVE_SPEED = 100


# =================================================
# FILE PATHS
# =================================================

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
    """Safe pause between movements."""
    time.sleep(seconds)


def speak(dog, text):
    """Speak and allow a short moment for the performance."""
    print(f"\nPiDog: {text}")
    dog.speak(text)


def safe_lie_down(dog):
    """
    Return PiDog to a stable recovery posture.
    """

    print("\n🛌 PiDog returning to safe lying posture...")

    try:
        dog.lie_down(speed=BODY_SPEED)
        pause(1.5)

    except Exception as error:
        print(f"⚠️ Lie-down recovery warning: {error}")


def safe_head_sequence(dog):
    """
    Slow head movement sequence.
    """

    dog.head_move(
        yaw=20,
        speed=HEAD_SPEED
    )
    pause(0.8)

    dog.head_move(
        yaw=-20,
        speed=HEAD_SPEED
    )
    pause(0.8)

    dog.head_move(
        yaw=0,
        speed=HEAD_SPEED
    )
    pause(0.8)


def safe_tail_sequence(dog, count=3):
    """
    Controlled tail wagging.
    """

    dog.wag_tail(
        count=count,
        speed=TAIL_SPEED
    )

    pause(1.0)


# =================================================
# HIGH FIVE HELPERS
# =================================================

def right_high_five(dog):
    """
    Right paw high-five.

    Uses the controller method if available.
    """

    print("\n✋ RIGHT PAW HIGH FIVE!")

    try:

        dog.set_light("yellow", bps=2)

        dog.high_five_right(
            speed=HIGH_FIVE_SPEED
        )

        pause(1.5)

    except AttributeError:

        print(
            "⚠️ high_five_right() is not available. "
            "Skipping right high-five."
        )

    except Exception as error:

        print(
            f"⚠️ Right high-five warning: {error}"
        )


def left_high_five(dog):
    """
    Left paw high-five.

    Uses the controller method if available.
    """

    print("\n✋ LEFT PAW HIGH FIVE!")

    try:

        dog.set_light("green", bps=2)

        dog.high_five_left(
            speed=HIGH_FIVE_SPEED
        )

        pause(1.5)

    except AttributeError:

        print(
            "⚠️ high_five_left() is not available. "
            "Skipping left high-five."
        )

    except Exception as error:

        print(
            f"⚠️ Left high-five warning: {error}"
        )


# =================================================
# CHRISTMAS SHOW
# =================================================

def run_christmas_show(dog):

    print("\n" + "=" * 60)
    print("STARTING SAFE CHRISTMAS PERFORMANCE")
    print("=" * 60)

    music = MusicPlayer()

    start_time = time.monotonic()

    try:

        # =============================================
        # PREPARE SAFE STARTING POSITION
        # =============================================

        print("\nPreparing PiDog...")

        dog.set_light(
            "red",
            bps=2
        )

        safe_lie_down(dog)

        # =============================================
        # START MUSIC
        # =============================================

        print("\n🎵 Starting Christmas music...")

        music.play(MUSIC_FILE)

        pause(1)

        # =============================================
        # SECTION 1 - CHRISTMAS GREETING
        # =============================================

        print("\n🎄 SECTION 1 - CHRISTMAS GREETING")

        dog.set_light(
            "red",
            bps=2
        )

        speak(
            dog,
            "Merry Christmas everyone! Welcome to my Christmas performance!"
        )

        pause(1)

        safe_head_sequence(dog)

        safe_tail_sequence(
            dog,
            count=3
        )

        safe_lie_down(dog)

        # =============================================
        # SECTION 2 - GREEN CHRISTMAS PERSONALITY
        # =============================================

        print("\n🎄 SECTION 2 - CHRISTMAS PERSONALITY")

        dog.set_light(
            "green",
            bps=2
        )

        safe_head_sequence(dog)

        safe_tail_sequence(
            dog,
            count=4
        )

        pause(1)

        safe_lie_down(dog)

        # =============================================
        # SECTION 3 - PUSH-UP MOMENT
        # =============================================

        print("\n💪 SECTION 3 - CHRISTMAS PUSH-UP")

        dog.set_light(
            "yellow",
            bps=2
        )

        speak(
            dog,
            "Let me show you one of my special moves!"
        )

        pause(1)

        print("\n💪 PiDog performing one controlled push-up...")

        try:

            dog.push_up(
                speed=PUSHUP_SPEED,
                repetitions=1
            )

            pause(2)

        except Exception as error:

            print(
                f"⚠️ Push-up warning: {error}"
            )

        safe_lie_down(dog)

        # =============================================
        # SECTION 4 - RIGHT HIGH FIVE
        # =============================================

        print("\n✋ SECTION 4 - RIGHT HIGH FIVE")

        speak(
            dog,
            "Would you like a Christmas high five?"
        )

        pause(1)

        right_high_five(dog)

        safe_lie_down(dog)

        # =============================================
        # SECTION 5 - LEFT HIGH FIVE
        # =============================================

        print("\n✋ SECTION 5 - LEFT HIGH FIVE")

        left_high_five(dog)

        safe_lie_down(dog)

        # =============================================
        # SECTION 6 - CHRISTMAS LIGHT SHOW
        # =============================================

        print("\n💡 SECTION 6 - CHRISTMAS LIGHT SHOW")

        dog.set_light(
            "red",
            bps=3
        )

        pause(2)

        dog.set_light(
            "green",
            bps=3
        )

        pause(2)

        dog.set_light(
            "yellow",
            bps=3
        )

        pause(2)

        dog.set_light(
            "blue",
            bps=3
        )

        pause(2)

        safe_head_sequence(dog)

        safe_tail_sequence(
            dog,
            count=4
        )

        safe_lie_down(dog)

        # =============================================
        # SECTION 7 - FINALE
        # =============================================

        print("\n🎅 SECTION 7 - CHRISTMAS FINALE")

        dog.set_light(
            "green",
            bps=3
        )

        speak(
            dog,
            "Thank you for watching my Christmas performance. Merry Christmas!"
        )

        pause(1)

        safe_head_sequence(dog)

        safe_tail_sequence(
            dog,
            count=5
        )

        # =============================================
        # FINAL SAFE POSITION
        # =============================================

        safe_lie_down(dog)

        dog.set_light(
            "green",
            bps=2
        )

        # =============================================
        # FINISH
        # =============================================

        elapsed = time.monotonic() - start_time

        print("\n" + "=" * 60)
        print("🎄 CHRISTMAS PERFORMANCE COMPLETE!")
        print(
            f"Total performance time: {elapsed:.1f} seconds"
        )
        print("=" * 60)

    finally:

        music.stop()

        print("\n🛌 Final safety reset...")

        try:
            safe_lie_down(dog)

        except Exception:
            pass