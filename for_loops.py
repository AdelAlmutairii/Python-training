# Makig max() function

students_scores = [] # Create an empty list 
for i in range(200):
    students_scores.append(i)
print(students_scores)

max_score = 0 # Create an empty counter to hold the largest number
for score in students_scores:
    if score > max_score:
        max_score = score # re assign the variable to the largest number you checked
print(max_score)
