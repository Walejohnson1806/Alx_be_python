def perform_operation(num1, num2, operation):
    """
    This function takes two numbers and an operation, then performs the math.
    It also makes sure to handle division by zero safely.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:  # Uh-oh, dividing by zero is not allowed!
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"