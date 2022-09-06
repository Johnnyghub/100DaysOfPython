student_scores = input("Input a list of student scores seperated by spaces: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_score = student_scores[0]
index = 0

for i in range(0, len(student_scores)):
    if student_scores[i] > max_score:
        max_score = student_scores[i]
        index = i

print(f"The highest score is {max_score} by student {index+1}.")
