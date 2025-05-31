students_score={"Harry":81,
                "Ron":78,
                "Hermione":99,
                "Draco":74,
                "Nerville":62,
}
students_score["Nina"]=93
students_score["Nerville"]=84
students_grades={}
for student in students_score:
    score= students_score[student]
    if students_score[student]>90:
       students_grades[student]="Out-standing"
    elif students_score[student]>80:
        students_grades[student] = "Exceeds expectations"
    elif students_score[student]>70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "fail"
for student in students_grades:
    print(student)
    print(students_grades[student])