import time
#from adafruit_circuitplayground import cp

morse_code = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '//' 
    }


message = input("What is the sentence you want to translate: ").lower()
try:
    unit_value = float(input("Enter the unit value (in milliseconds or seconds): "))
except ValueError:
    print("Enter a Valid input please!")

translated_message = []

# Translation 
for word in message.split():
    word_translation = []
    for char in word:
        if char in morse_code:
            word_translation.append(morse_code[char])
        else:
            print(f"Invalid character: {char}")
            exit()
    translated_message.append(' '.join(word_translation))
        


print(translated_message)

# Implementation to the circuit (Light and sound):

lettre = ''
for word in translated_message:
    for letter in word.split():
        for symbol in letter:
            if symbol == '.':
                print('.')
                time.sleep(unit_value)
            elif symbol == '-':
                print('-')
                time.sleep(3 * unit_value)
        print('_')
        time.sleep(3 * unit_value)
    print('//')
    time.sleep(7 * unit_value)
        

