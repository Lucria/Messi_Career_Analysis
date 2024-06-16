# Calculator Program
# The calculator must be able to perform addition, subtraction, multiplication and division.
# The calculator take in a continuous string of inputs from the user. The inputs will include either two numbers and an operator. An example of the input is "5 + 10" or "3 * 6".
# The operators will only be +, -, * or /.
# The calculator program will then perform the calculation and print out the result to the user.


maths = input("Please write: ") # "5 + 10"
numbers = maths.split()

# Check if the user input is valid
if len(numbers) != 3:
    print("Invalid input")
    exit()

num1, operator, num2 = numbers

num1 = float(num1)
num2 = float(num2)

# Perform the calculation based on the operator (+, -, *, /)
if operator == "+":
    answer =  num1 + num2
elif operator == "-":
    answer = num1 - num2
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    answer = num1 / num2
else:
    print("error!")

print(' ')
print(f'your answer is {answer}.')

