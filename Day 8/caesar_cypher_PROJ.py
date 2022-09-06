letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

logo = ''' 
██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
██║     ███████║█████╗  ███████╗███████║██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     
██║     ██║██████╔╝███████║█████╗  ██████╔╝     
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗     
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝'''

print(f"\033[31m{logo}\033[00m\n")
direction = ''
text = ''
shift = ''
cont = True


def input_prompt():
    global direction, text, shift, cont
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt. Type anything else to exit:\n").lower()

    if (direction != 'encode') and (direction != 'decode'):
        cont = False  # incase quit() doesn't work
        print("\nThank you for using the caesar cypher python program!")
        quit()

    text = input("Type your message:\n").lower()

    shift = ''

    while shift == '':
        try:
            shift = int(input("Type the shift number:\n"))
        except:
            print("Please enter an integer for shift.\n")
            shift = ''

    shift %= 26  # even if shift is not out of range, there is no harm in finding the modulus as it will remain the same


def caesar(original_text, shift_amount, cipher_direction):
    new_text = ""

    for char in original_text:
        if char in letters:
            if cipher_direction == 'encode':
                index = letters.index(char) + shift_amount

                if index > (len(letters)-1):  # to avoid index errors
                    index -= len(letters)  # goes around the letters array to start back at the beginning
            else:
                index = letters.index(char) - shift_amount

                if index < 0:
                    index += len(letters)  # same logic as forward shift, except this time we loop back around to the end

            new_text += letters[index]
        else:  # if it is not a letter, do not shift
            new_text += char

    print(f"\nThe {cipher_direction}d text is {new_text}.")


while cont:
    input_prompt()
    caesar(text, shift, direction)
