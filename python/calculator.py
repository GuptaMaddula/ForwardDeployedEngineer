def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

do_perform=False
num1 = float(input("Enter the first number: "))
while not do_perform:
    
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    if operation == "+":
        perform_operation = add
    elif operation == "-":
        perform_operation = subtract
    elif operation == "*":
        perform_operation = multiply
    elif operation == "/":
        perform_operation = divide

    result = perform_operation(num1, num2)
    print(f"The result of {num1} {operation} {num2} is: {result}")
    num1=result
    continue_calculation = input("Type 'yes' to continue calculating with the result, or 'no' to exit: ").lower()
    if continue_calculation != "yes":
        do_perform = True
        print("Exiting the calculator. Goodbye!")