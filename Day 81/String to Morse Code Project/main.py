# this is a dictionary containing all letters and numbers and some punctuation in morse code

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

string_to_convert = input("Please enter the string you would like to turn into Morse Code: ")

morse_code = ""
could_not_encode = 0  # the number of characters not available in the dictionary

for char in string_to_convert:
    try:
        if char != " ":
            # 1 space for seperation between letters
            morse_code += MORSE_CODE_DICT[char.upper()] + " "  # add the morse code for anything except a space
        else:
            morse_code += " "  # otherwise add an extra space to show seperation between words
    except KeyError:
        could_not_encode += 1  # if the character is not found, just ignore it, no necessary english character is not found in our dictionary

if could_not_encode > 0:
    print(f"Could not find {could_not_encode} characters in the dictionary.")
print(f"That string in morse code is: \n{morse_code}")
