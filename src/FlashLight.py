import time

class FlashLight:

    dot_light_duration = 100  # Milliseconds
    dash_light_duration = dot_light_duration * 3

    @classmethod
    def decode(cls, morse_code):
        for char in morse_code:
            if char == ".":
                cls.turn_on(cls.dot_light_duration)
            elif char == "-":
                cls.turn_on(cls.dash_light_duration)

    @classmethod
    def turn_on(cls, duration):
        print("On")
        time.sleep(duration / 1000)
        cls.turn_off()
    
    @classmethod
    def turn_off(cls):
        print("Off")
