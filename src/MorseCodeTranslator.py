import sys
import time
from MorseCodeDictionnary import *
from Speaker import *


class MorseCodeTranslator:

    TIME_BETWEEN_CHAR = 1.2

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
    if len(sys.argv) > 1:
        text_file = sys.argv[1]
    else:
        text_file = "text_example.txt"

    MorseCodeTranslator.translate_from_text_file(text_file)
