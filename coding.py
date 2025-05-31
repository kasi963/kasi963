age=input("what is your age?")
current_age=int(age)
new_age=90-current_age
days_age=365*new_age
weeks_age=new_age*52
months_age=new_age*12
print("you have " + str(days_age) + " days and\n " + str(weeks_age) + " weeks and\n" + str(months_age)+" months left")