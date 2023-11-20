username = input("What is your name? >>> ")
weight = float(input("How much do you weigh (pounds/lb)? >>> "))
height = float(input("How tall are you (inches/in)? >>> "))
bmi = weight/height**2 * 703
print(f"{username}, your BMI is {bmi:.2f}")

