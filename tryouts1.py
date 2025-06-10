import random
for i in range(5):
 users_choice=int(input("Guess the number:"))
 computers_choice=random.randint(1,10)
 if users_choice>computers_choice:
    print("oops, that is too high" + f" the computer chose {computers_choice}")
 elif users_choice<computers_choice:
    print( "ugh,too low.. try harder" + f" the computer chose {computers_choice}")
 else:
    print("great guess! try another one")
