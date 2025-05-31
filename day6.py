#while loop
names=6
while names >0:
    name_students=input("what is your name?\n")
    names-=1
    print("Hello",name_students)

def my_function():
    name=input("what is your name?\n")
    if name == "john":
        print("Hello John")
    else:
        print(name)
my_function()