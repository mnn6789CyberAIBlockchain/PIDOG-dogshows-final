"""
PiDog Final Project
Cross-Platform Music Player

Plays WAV music files during PiDog performances.

Windows:
    Uses winsound.

Linux / Raspberry Pi:
    Uses aplay.
"""

import os
import platform
import subprocess
import threading
import winsound


class MusicPlayer:

    def __init__(self):

        self.process = None
        self.system = platform.system()


    # =================================================
    # PLAY MUSIC
    # =================================================

    def play(self, music_file):

        # Stop existing music first
        self.stop()

        if not os.path.exists(music_file):

            print(f"Music file not found: {music_file}")

            return

        print(f"Playing music: {music_file}")

        # =============================================
        # WINDOWS
        # =============================================

        if self.system == "Windows":

            try:

                self.process = threading.Thread(
                    target=winsound.PlaySound,
                    args=(
                        music_file,
                        winsound.SND_FILENAME
                    ),
                    daemon=True
                )

                self.process.start()

            except Exception as error:

                print(f"Windows music error: {error}")


        # =============================================
        # LINUX / RASPBERRY PI
        # =============================================

        else:

            try:

                self.process = subprocess.Popen(
                    ["aplay", music_file]
                )

            except FileNotFoundError:

                print(
                    "Audio player not available."
                )


    # =================================================
    # STOP MUSIC
    # =================================================

    def stop(self):

        if self.process is None:

            return

        print("Stopping music...")

        # =============================================
        # WINDOWS
        # =============================================

        if self.system == "Windows":

            try:

                winsound.PlaySound(
                    None,
                    winsound.SND_PURGE
                )

            except Exception:

                pass


        # =============================================
        # LINUX / RASPBERRY PI
        # =============================================

        else:

            try:

                self.process.terminate()

                self.process.wait(timeout=2)

            except Exception:

                try:

                    self.process.kill()

                except Exception:

                    pass

        self.process = None