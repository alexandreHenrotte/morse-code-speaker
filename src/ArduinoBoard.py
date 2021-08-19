import pyfirmata

class ArduinoBoard:

    # THOSE VALUES MIGHT CHANGE BASE ON YOUR PHYSICIAL ENVIRONMENT
    ARDUINO_COM_PORT = "COM4"
    BUZZER_PIN = 2

    @classmethod
    def connect(cls):
        cls.board = pyfirmata.Arduino(cls.ARDUINO_COM_PORT)
        cls.buzzer = cls.board.get_pin('d:' + str(cls.BUZZER_PIN) + ':o')

    @classmethod
    def disconnect(cls):
        cls.board.exit()