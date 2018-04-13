rpio = True
try:
    import RPi.GPIO as GPIO
except ImportError as e:
    rpio = False

from time import sleep

class PINS:
    GPIO02 = 2
    GPIO03 = 3
    GPIO04 = 4
    GPIO05 = 5
    GPIO06 = 6
    GPIO07 = 7
    GPIO08 = 8
    GPIO09 = 9
    GPIO10 = 10
    GPIO11 = 11
    GPIO12 = 12
    GPIO13 = 13
    GPIO14 = 14
    GPIO15 = 15
    GPIO16 = 16
    GPIO17 = 17
    GPIO18 = 18
    GPIO19 = 19
    GPIO20 = 20
    GPIO21 = 21
    GPIO22 = 22
    GPIO23 = 23
    GPIO24 = 24
    GPIO25 = 25
    GPIO26 = 26
    GPIO27 = 27

pinList = [vars(PINS)[item] for item in vars(PINS) if not item.startswith("__")]

CODES = {
    'a': ".-",
    'b': "-...",
    'c': "-.-.",
    'd': "-..",
    'e': ".",
    'f': "..-.",
    'g': "--.",
    'h': "....",
    'i': "..",
    'j': "",
    'k': "",
    'l': ".-..",
    'm': "--",
    'n': "-.",
    'o': "---",
    'p': ".--.",
    'q': "--.-",
    'r': ".-.",
    't': "-",
    'u': "..-",
    'v': "...-",
    'w': ".--",
    'x': "-..-",
    'y': "-.--",
    'z': "--..",
    '0': "-----",
    's': "...",
    '1': ".----",
    '2': "..---",
    '3': "...--",
    '4': "....-",
    '5': ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
    '.': ".-.-.-",
    '(': "-.--.-",
    ',': "--..--",
    ':': "---...",
    '?': "..--..",
    '\'': ".----.",
    '-': "-....-",
    '/': "-..-.",
    ')': "-.--.-",
    '"': ".-..-.",
    '@': ".--.-.",
    '=': "-...-",
}

def setup():
    if rpio:
        GPIO.setmode(GPIO.BCM) # Using the broadcom numbers
        GPIO.setup(pinList, GPIO.OUT) # Configure all pins for output

def cleanup():
    if rpio:
        GPIO.output(pinList, GPIO.LOW) # Ensure all pins are off
        GPIO.cleanup()

def pinHigh(pin:int):
    if rpio:
        GPIO.output(pin, GPIO.HIGH)

def pinLow(pin:int):
    if rpio:
        GPIO.output(pin, GPIO.LOW)

def parseLine(line:str) -> str:
    code = ""
    for c in line:
        if c == ' ':
            code += "WORD"
            continue

        code += getCode(c.lower())

        if c == '.':
            code += "STOP"

        code += ' '

    return code

def getCode(alphaNumeric:chr) -> str:
    return CODES.get(alphaNumeric, '')

def outputCode(code:str, pin:int):
    if rpio:
        DELAY = 250 /1000 # Set the number of seconds to delay

        splitByStop = code.split("STOP")
        for line in splitByStop:
            words = line.split("WORD")

            for word in words:
                chars = word.split(" ")

                for code in chars:
                    for dotOrDash in code:
                        pinHigh(pin)

                        if dotOrDash == '.': sleep(DELAY)
                        else: sleep(DELAY*3)

                        pinLow(pin)
                        sleep(DELAY)

                sleep(DELAY*2)

            sleep(DELAY*4)
