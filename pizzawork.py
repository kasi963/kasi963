print("Welcome to python pizza deliveries!")
small=15
medium=20
large=25
peperoni=2
cheese=1
pizza_size=input("What pizza size do you want?\n")
if pizza_size == "small":
    Bill=small
    print("small size is $",small)
elif pizza_size == "medium":
    Bill=medium
    print("medium size is $",medium)
elif pizza_size == "large":
    Bill=large
    print("large size is $",large)
add_peperoni=input("Would you like to add peperoni?\n")
if add_peperoni == "yes":
    if pizza_size == "small":
        Bill+=2
    else:
        Bill+=3
cheese=input("Do you want cheese?\n")
if cheese == "yes":
    Bill+=1
print("Your final bill is $", Bill)




