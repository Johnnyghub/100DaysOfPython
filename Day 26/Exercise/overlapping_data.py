with open("numbers1.txt") as file1:
    data1 = file1.readlines()

with open("numbers2.txt") as file2:
    data2 = file2.readlines()

data = [int(i.strip()) for i in data1 if i in data2]

print(data)
