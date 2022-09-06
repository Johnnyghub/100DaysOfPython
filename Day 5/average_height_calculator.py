student_heights = input("Input a list of student heights in cm seperated by spaces: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum_of_heights = 0
counter = 0

for i in range(0, len(student_heights)):
    sum_of_heights += student_heights[i]
    counter += 1

print(f"Average height of the group of students: {round(sum_of_heights/counter)} cm.")
