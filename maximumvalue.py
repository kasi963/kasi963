student_score=input("what are your scores?\n").split(',')
for n in range(0,len(student_score)):
 student_score[n] = int(student_score[n])
print(student_score)
maximum_score=0
for score in student_score:
 if score>maximum_score:
  maximum_score=score
print("The maximum score is",maximum_score)



