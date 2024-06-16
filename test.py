def calculator():
    print("Simple Calculator")
    print("Enter 'q' to quit")

    while True:
        # Take input from the user
        user_input = input("Enter calculation (e.g., 5 + 10): ")

        # Check if the user wants to quit
        if user_input.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            # Split the user input into components
            parts = user_input.split()

            if len(parts) != 3:
                raise ValueError("Invalid input format. Please enter in the format: number1 operator number2")

            num1, operator, num2 = parts

            # Convert the string numbers to floats
            num1 = float(num1)
            num2 = float(num2)

            # Perform the calculation based on the operator
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ValueError("Division by zero is not allowed")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator. Please use one of the following: +, -, *, /")

            # Print the result
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")

# Run the calculator
calculator()
