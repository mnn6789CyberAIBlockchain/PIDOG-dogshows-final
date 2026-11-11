
"""
PiDog Final Project - Hardware Controller

Controls the real SunFounder PiDog hardware.

This controller provides:
- Basic movement
- Preset actions
- Head movement
- Tail movement
- RGB lights
- Safe cleanup
"""


class PiDogController:

    def __init__(self):

        self.dog = None
        self.connected = False

        try:
            from pidog import Pidog

            print("🐶 Connecting to PiDog hardware...")

            self.dog = Pidog()

            self.connected = True

            print("✅ PiDog connected!")

        except Exception as error:

            print("⚠️ PiDog hardware not available.")
            print(f"Reason: {error}")


    # =================================================
    # CONNECTION STATUS
    # =================================================

    def is_connected(self):

        return self.connected


    # =================================================
    # GENERAL ACTION
    # =================================================

    def action(self, name, speed=150, step_count=1):

        if not self.connected:
            print(
                f"🐶 [SIMULATION] Action: {name} "
                f"Speed={speed} Steps={step_count}"
            )
            return

        print(f"🐶 Performing action: {name}")

        self.dog.do_action(
            name,
            step_count=step_count,
            speed=speed
        )

        self.dog.wait_all_done()


    # =================================================
    # BASIC MOVEMENTS
    # =================================================

    def sit(self, speed=150):

        self.action("sit", speed=speed)


    def stand(self, speed=150):

        self.action("stand", speed=speed)


    def stretch(self, speed=180):

        self.action("stretch", speed=speed)


    def forward(self, steps=1, speed=180):

        self.action(
            "forward",
            speed=speed,
            step_count=steps
        )


    def backward(self, steps=1, speed=180):

        self.action(
            "backward",
            speed=speed,
            step_count=steps
        )


    def turn_left(self, steps=1, speed=180):

        self.action(
            "turn_left",
            speed=speed,
            step_count=steps
        )


    def turn_right(self, steps=1, speed=180):

        self.action(
            "turn_right",
            speed=speed,
            step_count=steps
        )


    def trot(self, steps=1, speed=190):

        self.action(
            "trot",
            speed=speed,
            step_count=steps
        )


    def push_up(self, speed=180, repetitions=1):

        self.action(
            "push_up",
            speed=speed,
            step_count=repetitions
        )


    # =================================================
    # HEAD MOVEMENT
    # =================================================

    def head_move(
        self,
        yaw=0,
        roll=0,
        pitch=0,
        speed=180
    ):

        if not self.connected:

            print(
                f"👀 [SIMULATION] Head → "
                f"Yaw={yaw}, Roll={roll}, Pitch={pitch}"
            )

            return

        self.dog.head_move(
            [[yaw, roll, pitch]],
            immediately=True,
            speed=speed
        )

        self.dog.wait_head_done()


    def head_shake(self, speed=190):

        self.action(
            "shake_head",
            speed=speed
        )


    # =================================================
    # TAIL MOVEMENT
    # =================================================

    def wag_tail(self, count=5, speed=180):

        self.action(
            "wag_tail",
            speed=speed,
            step_count=count
        )


    # =================================================
    # RGB LIGHTS
    # =================================================

    def set_light(self, color="red", bps=1):

        if not self.connected:

            print(
                f"💡 [SIMULATION] Light → {color}"
            )

            return

        self.dog.rgb_strip.set_mode(
            "breath",
            color,
            bps=bps
        )


    # =================================================
    # STOP
    # =================================================

    def stop(self):

        if not self.connected:
            return

        print("🛑 Stopping PiDog...")

        try:
            self.dog.wait_all_done()

        except Exception:
            pass


    # =================================================
    # CLEANUP
    # =================================================

    def close(self):

        if self.connected and self.dog:

            print("🐶 Closing PiDog connection...")

            self.dog.close()

            self.connected = False
