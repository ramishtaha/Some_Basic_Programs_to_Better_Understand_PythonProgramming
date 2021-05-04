# Greetings.
print("Welcome to the Life in Weeks Calculator")

# Below code Calculates How many years you have till you turn 90 and stores it in a variable.
age = int(input("Please Enter Your Current Age:\n"))
yrs_remaining = 90 - age

# Below code Calculates the number of Days, Weeks, Years from the above calculated variable.
days = yrs_remaining * 365
weeks = yrs_remaining * 52
months = yrs_remaining * 12

# Below code uses f-string to properly format all the above calculated Variables.
print(f"You have {days} days, {weeks} weeks, {months} months and {yrs_remaining} Years left.")