print("Welcome to BMI Calculator")

# Take Inputs from the user(String) and Typecasting the UserInput to Float
height = float(input("Enter your height in Meters: "))
weight = float(input("Enter your Weight in Kilograms: "))

# Calculate the BMI.
bmi = (weight / (height ** 2))

# Round the Calculated BMI, Type Casting it to a String and then Concatenate Both the Strings.
print("Your BMI(Body Mass Index) is: " + str(round(bmi)))
