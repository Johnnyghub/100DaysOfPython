with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open('Input/Letters/starting_letter.txt') as sample:
    sample_letter = sample.read()

for name in names:
    name = name.strip()
    with open(file=f"Output/ReadyToSend/LetterFor{name}.txt", mode='w') as letter:
        formatted_letter = sample_letter.replace("[name]", name)
        letter.write(formatted_letter)
