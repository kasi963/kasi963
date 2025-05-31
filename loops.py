students_height=input("enter the heights\n").split(',')
for n in range(0,len(students_height)):
    students_height[n] = int(students_height[n])
print(students_height)
total = 0
count = 0
for height in students_height:
    total += height
    count +=1
    average = round(total/count)
    print("the average height is",average)