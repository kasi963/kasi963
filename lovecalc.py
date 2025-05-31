print("welcome to the love calculator!")
name1=input("enter the first name? ")
name2=input("enter the second name? ")
combined_names=name1+name2
lower_case=combined_names.lower()
t=lower_case.count('t')
r=lower_case.count('r')
u=lower_case.count('u')
e=lower_case.count('e')
true=t+r+u+e
l=lower_case.count('l')
o=lower_case.count('o')
v=lower_case.count('v')
e=lower_case.count('e')
love=l+o+v+e
love_score=true + love
if love_score<10 or love_score>90:
    print("your score is",str(love_score),"you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
        print("Your score is:",str(love_score),"You will do alright together")
else:
        print("Your score is:",str(love_score))


