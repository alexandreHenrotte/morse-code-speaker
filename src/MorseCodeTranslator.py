import sys
import time
from MorseCodeDictionnary import *
from Speaker import *
from ArduinoBoard import *


class MorseCodeTranslator:

    TIME_BETWEEN_CHAR = 0.8

    @classmethod
    def translate_from_text_file(cls, filepath):
        file = open(filepath, "r")
        for line in file:
            for word in line.split(" "):
                for char in word:
                    try:
                        morse_code = cls.get_morse_code(char)
                        Speaker.decode(morse_code)
                        time.sleep(cls.TIME_BETWEEN_CHAR)
                    except:
                        print(repr(char) +
                              " cannot be convert into morse code --> ignore character...")
                print("\r\n")

    @classmethod
    def get_morse_code(cls, char):
        morse_code = morse_code_dictionnary[char.upper()]
        print(char + " : " + morse_code)
        return morse_code


if __name__ == "__main__":
    # Check if filename is given as cmd argument
    if len(sys.argv) > 1:
        text_file = sys.argv[1]
    # Else take default file
    else:
        text_file = "text_example.txt"

    try:
        # Connect the ArduinoBoard class to the physical arduino
        ArduinoBoard.connect()
        # Iterate file and translate to binary
        MorseCodeTranslator.translate_from_text_file(text_file)
    except Exception as e:
        print(e)
    finally:
        # Disconnect the ArduinoBoard class of the physical arduino
        ArduinoBoard.disconnect()