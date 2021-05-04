# Greeting Message
print("Welcome to The Digits sum Calculator!!\n")

# Inputting from console and storing it to a Variable.
num = input("Enter a Number: ")
sum = 0

# This for loop takes each element from the string, changes it's type to int and then adds it to the sum variable.
for i in num:
    sum += int(i)

# At last we print the sum.
print("The Sum of the Digits is: " + str(sum))
