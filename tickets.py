print("hello and welcome to my rollercoaster!")
height=float(input("enter your height:"))
Bill=0
if height>=120:
    print("you can ride the rollercoaster!")
    age = int(input("enter your age:"))
    if age < 12:
        Bill = 3
        print("children tickets are $3")
    elif age <= 18:
        Bill = 7
        print("standard tickets are $7")
    elif age >= 45 and age <= 55:
        print("your ticket is $0")
    else:
        Bill = 12
        print("Adult tickets are $12")
    photo = input("Do you want a photo taken? Yes or No:")
    if photo == "Yes":
      Bill+=3
    print("your bill is $", Bill)
else:
    print("You're too short!")







