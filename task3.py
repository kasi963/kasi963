from xmlrpc.client import Boolean

print("Welcome to the rollercoaster!")
height=float(input("Enter your height:\n"))
if height>=120:
    print("You can ride the roller!")
    age = int(input("what is your age?\n"))
    if age < 12:
        print("Your ticket price is $4")
    if age >= 18:
        print("Your ticket price is $7")
    elif age>=15:
        print("Your ticket price is $6")
else:
    print("Sorry, you're too short!")


