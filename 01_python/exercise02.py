number1 = float(input("Enter first number: "))
operation = input("Choose operation: ")
number2 = float(input("Enter second number: "))
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Division by zero!")
else:
    print("Wrong operation!")