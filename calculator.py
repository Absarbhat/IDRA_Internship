# Program to perform basic arithmetic operations on two numbers

# Accept input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

# Display the results
print("\n----- Arithmetic Operations -----")
print(f"Addition (+): {num1} + {num2} = {addition}")
print(f"Subtraction (-): {num1} - {num2} = {subtraction}")
print(f"Multiplication (*): {num1} * {num2} = {multiplication}")
print(f"Division (/): {num1} / {num2} = {division}")
print(f"Floor Division (//): {num1} // {num2} = {floor_division}")
print(f"Modulus (%): {num1} % {num2} = {modulus}")
print(f"Exponentiation (**): {num1} ** {num2} = {exponentiation}")