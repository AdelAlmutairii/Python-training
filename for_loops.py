students_scores = []
for i in range(200):
    students_scores.append(i)
print(students_scores)

max_score = 0
for score in students_scores:
    if score > max_score:
        max_score = score
print(max_score)