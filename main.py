# This program takes 3 numbers, asks the user if they want to add or subtract the 2nd number to the 1st, then asks the user if they want to multiply or divide that number by
# the 3rd number, and depending on the sum of that result, it will give the user a reward of Platinum, Gold, Silver, Bronze, or no reward :(

num1 = int(input("Please input Number 1: "))
num2 = int(input("Please input Number 2: "))
num3 = int(input("Please input Number 3: "))

addorsub = input("Would you like to add or subtract Number 2 to Number 1? ")
if addorsub == "add" or addorsub == "Add":
    num4 = (num1 + num2)
    print("This new number shall be known as Number 4.")
elif addorsub == "subtract" or addorsub == "Subtract":
    num4 = (num1 - num2)
    print("This new number shall be known as Number 4.")
else:
    print("Invalid input. Reset program.")

mulordiv = input("Would you like to multiply or divide Number 4 by Number 3? ")
if mulordiv == "multiply" or mulordiv == "Multiply":
    num5 = (num4 * num3)
    print("This new number shall be known as Number 5.")
elif mulordiv == "divide" or mulordiv == "Divide":
    num5 = (num4 / num3)
    print("This new number shall be known as Number 5.")
else:
    print("Invalid input. Reset program.")

if num5 >= 5000:
    print("Reward: Platinum")
elif num5 >= 4000:
    print("Reward: Gold")
elif num5 >= 3000:
    print("Reward: Silver")
elif num5 >= 2000:
    print("Reward: Bronze")
else:
    print("No reward :(")