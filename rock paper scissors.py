print("Welcome to Rock paper scissors!")
users_choice=int(input("pick a choice:\n 0 for rock\n 1 for paper\n 2 for scissors\n"))
game_images=["rock","paper","scissors"]
print(game_images[users_choice])
import random
computer_choice=random.randint(0,2)
if computer_choice>=3 and users_choice<0:
    print("you typed an invalid choice")
elif computer_choice == 0 and users_choice == 2:
    print("Computer chose rock so computer won")
elif computer_choice ==2 and users_choice == 0:
    print("user wins!")
elif computer_choice>users_choice:
    print("oops,computer won!")
elif computer_choice<users_choice:
    print("user wins!")
elif computer_choice == users_choice:
    print("its a draw!")
else:
    print("please choose a valid choice")


