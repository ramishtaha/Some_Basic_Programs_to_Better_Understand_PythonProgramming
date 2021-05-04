# Greetings
print("Welcome To The Tip Calculator")

# Input bill amount, the percentage of tip you want to give and the number of Friends.
bill_amt = int(input("Please Enter the Bill amount\n$"))
tip_percent = int(input("Please Enter the Percentage of Tip you Wanna give? (Example 10, 12 or 14): "))
peoples = int(input("Please Enter the number of Friends you wanna Split bill with: "))

# Calculate the Tip and Share of each friend.
tip = (bill_amt * tip_percent / 100)
person_share = (bill_amt + tip) / peoples

# Print out how much each friend should pay using f-string.
print(f"Each of you should pay ${person_share}")
