import winsound
from threading import Thread


class Speaker:

    sound_frequency = 600  # Hertz
    dot_sound_duration = 100  # Milliseconds
    dash_sound_duration = dot_sound_duration * 3

    @classmethod
    def play(cls, morse_code):
        for char in morse_code:
            if char == ".":
                Thread(target=cls.play_dot_sound).start()
                # cls.play_dot_sound()

            elif char == "-":
                Thread(target=cls.play_dash_sound).start()
                # cls.play_dash_sound()

    @classmethod
    def play_dot_sound(cls):
        winsound.Beep(cls.sound_frequency, cls.dot_sound_duration)

    @classmethod
    def play_dash_sound(cls):
        winsound.Beep(cls.sound_frequency, cls.dash_sound_duration)
