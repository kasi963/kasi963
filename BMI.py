height=float(input("enter your height in m:"))
weight=float(input("Enter your weight in kg:"))
bmi= round (weight/(height**2))
if bmi<18.5:
    print(f"Your BMI is {bmi}\n" + "You're underweight.")
elif bmi<25:
    print(f"your BMI is {bmi}\n" + "you're normal weight.")
elif bmi<30:
        print(f"Your BMI is {bmi}\n" + "you're overweight.")
elif bmi<35:
            print(f"your BMI is {bmi}\n" + "you're obese.")
else:
            print(f"your BMI is {bmi}\n" + "you are clinically obese.")
