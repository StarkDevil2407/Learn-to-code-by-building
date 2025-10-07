# Exception Handling in Python

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Oops! That's not a valid number.")
finally:
    print("Program finished.")
