print("1: Add, 2: Subtract, 3: Multiply, 4: Divide")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = int(input("Enter operation (1-4): "))



if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    result = num1 * num2
elif operation == 4:
    result = num1 / num2 if num2 != 0 else "Error"
else:
    result = "Invalid"

print("Result:", result)