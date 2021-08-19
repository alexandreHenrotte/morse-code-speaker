import time
from threading import Thread
from ArduinoBoard import *

class Speaker:

    dot_sound_duration = 0.2  # Seconds
    dash_sound_duration = dot_sound_duration * 3

    @classmethod
    def decode(cls, morse_code):
        for char in morse_code:
            if char == ".":
                Thread(target=cls.play_dot_sound).start()
                # cls.play_dot_sound()

            elif char == "-":
                Thread(target=cls.play_dash_sound).start()
                # cls.play_dash_sound()

    @classmethod
    def play_dot_sound(cls):
        cls._play_sound(cls.dot_sound_duration)

    @classmethod
    def play_dash_sound(cls):
        cls._play_sound(cls.dash_sound_duration)

    @classmethod
    def _play_sound(cls, duration):
        t_end = time.time() + duration
        while time.time() < t_end:
            ArduinoBoard.buzzer.write(True)
        ArduinoBoard.buzzer.write(False)