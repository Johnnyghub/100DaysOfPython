validInput = False
firstNumber = 0
secondNumber = 0
even_sum = 0

print("This program will add all the even numbers in the range of the 2 numbers you provide.\n")

while not validInput:
    try:
        firstNumber = int(input("Enter the first integer: "))
        secondNumber = int(input("Enter the second integer: "))
        validInput = True
    except:
        print("Please enter only integers.\n")

if secondNumber < firstNumber:  # to make sure range function works
    temp = firstNumber
    firstNumber = secondNumber
    secondNumber = temp

startingNumber = firstNumber  # need a new variable so we can keep the original number in the print statement

if firstNumber % 2 == 1:
    startingNumber += 1  # make first number even so we can start the for loop with it

for i in range(firstNumber, secondNumber+1, 2):
    even_sum += i

print(f"The sum of all the even numbers between {firstNumber} and {secondNumber} is {even_sum}.")
