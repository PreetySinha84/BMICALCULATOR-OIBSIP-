weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meter:"))
bmi = weight/(height **2)
print("your BMI is:",bmi)
if bmi<18.5:
    print("you are underweight")
elif 18.5<=bmi<25:
    print("you are a normal weight")
elif 25<=bmi<30:
    print("you are overweight")