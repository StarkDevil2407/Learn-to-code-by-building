# List Comprehensions in Python

numbers = [1, 2, 3, 4, 5, 6]
squares = [n**2 for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", even_numbers)
