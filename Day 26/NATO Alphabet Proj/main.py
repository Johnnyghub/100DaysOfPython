import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

word = input("Enter a word to convert to NATO format: ")

nato_string = ""

for letter in word:
    try:
        nato_string += f"{nato_dict[letter.upper()]} "
    except:
        nato_string += f"{letter} "  # if letter not in dict, print it normally (spaces, numbers, etc)

print(nato_string)
