#tip calculator
print("welcome to the tip calculator!")
Bill=float(input("what was the total bill?"))
tip=int(input("what percentage tip would you like to give? 10, 12 0r 15\n"))
people=int(input("how many people to split the bill?\n"))
tip_percent=tip/100
total_tip=tip_percent*Bill
total_Bill=Bill+total_tip
Bill_per_person=total_Bill/people
final=round(Bill_per_person,2)
print(f"each person has a total of ${final}")
