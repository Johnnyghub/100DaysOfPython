lowerRange = 1
higherRange = 100

for i in range(lowerRange, higherRange + 1):
    output = ""

    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"

    if output == "":
        output = str(i)

    print(output)
