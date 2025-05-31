print("Welcome to treasure island!\n" + "Your mission is to find the treasure!")
print("Are you ready to go?\n"+ "lets begin!")
direction=input("where do you want to go? left or right?")
if direction=="right":
    print("sorry! game over!")
elif direction=="left":
    challenge1=input("you've arrived at a lake, will you swim or wait?")
    if challenge1=="swim":
        print("You just became food for the crocodile")
    elif challenge1=="wait":
        print("you're almost there!")
        final_challenge=input("A boat took you to a house, there are three doors red, blue and yellow\n" + "pick one door")
        if final_challenge=="red":
            print("oops! there is a snake here!")
        elif final_challenge=="blue":
            print("You just got attacked by a bear!\n you lose!")
        else:
            print("You won! headover to the link below for your prize")
