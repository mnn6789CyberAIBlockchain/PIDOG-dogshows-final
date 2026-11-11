"""
PiDog Final Project
Cross-Platform Music Player

Windows:
    Uses winsound for WAV playback.

Raspberry Pi / Linux:
    Uses aplay for WAV playback.
"""

import os
import platform
import subprocess


class MusicPlayer:

    def __init__(self):

        self.process = None
        self.system = platform.system()


    def play(self, music_file):

        # Stop currently playing music first
        self.stop()

        # Convert to an absolute path
        music_file = os.path.abspath(music_file)

        if not os.path.exists(music_file):

            print(f"Music file not found: {music_file}")

            return

        print(f"Playing music: {music_file}")


        # =============================================
        # WINDOWS
        # =============================================

        if self.system == "Windows":

            try:

                self.process = subprocess.Popen(
                    [
                        "powershell",
                        "-c",
                        (
                            "Add-Type -AssemblyName presentationCore; "
                            "$player = New-Object "
                            "System.Windows.Media.MediaPlayer; "
                            f"$player.Open([uri]'{music_file}'); "
                            "$player.Play(); "
                            "Start-Sleep -Seconds 120"
                        )
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

            except Exception as error:

                print(f"Windows audio error: {error}")


        # =============================================
        # LINUX / RASPBERRY PI
        # =============================================

        elif self.system == "Linux":

            try:

                self.process = subprocess.Popen(
                    ["aplay", music_file]
                )

            except FileNotFoundError:

                print(
                    "Audio player 'aplay' was not found."
                )

                print(
                    "Install ALSA utilities:"
                )

                print(
                    "sudo apt install alsa-utils"
                )


        # =============================================
        # OTHER SYSTEMS
        # =============================================

        else:

            print(
                f"Unsupported operating system: "
                f"{self.system}"
            )


    def stop(self):

        if self.process is not None:

            print("Stopping music...")

            try:

                self.process.terminate()

                self.process.wait(timeout=3)

            except subprocess.TimeoutExpired:

                self.process.kill()

            except Exception:

                pass

            finally:

                self.process = None