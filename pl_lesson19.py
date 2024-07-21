# Calculator Program
# The calculator must be able to perform addition, subtraction, multiplication and division.
# The calculator take in a continuous string of inputs from the user. The inputs will include either two numbers and an operator. An example of the input is "5 + 10" or "3 * 6".
# The operators will only be +, -, * or /.
# The calculator program will then perform the calculation and print out the result to the user.
import tkinter
from tkinter import font

def calculate():
    # maths = input("Please write: ") # "5 + 10"
    maths = entry.get()

    numbers = maths.split()

    # Check if the user input is valid
    if len(numbers) < 3 or len(numbers) % 2 == 0:
        result_label.config(text="Invalid Input")
        return

    total = float(numbers[0])
    operator_index = 1

    for i in range(2, len(numbers), 2):
        operator = numbers[operator_index]
        num2 = float(numbers[i])

        if operator == "+":
            total += num2
        elif operator == "-":
            total -= num2
        elif operator == "*":
            total *= num2
        elif operator == "/":
            if num2 == 0:
                result_label.config(text="You just divided by zero!")
                return
            total /= num2
        else:
            result_label.config(text="Invalid Operator!")
            return

        operator_index += 2

    result_label.config(text=f'Result: {total}')

    # # Check if the user input is valid
    # if len(numbers) != 3:
    #     # print("Invalid input")
    #     result_label.config(text="Invalid Input")
    #     return

    # num1, operator, num2 = numbers

    # num1 = float(num1)
    # num2 = float(num2)

    # # Perform the calculation based on the operator (+, -, *, /)
    # if operator == "+":
    #     answer =  num1 + num2
    # elif operator == "-":
    #     answer = num1 - num2
    # elif operator == "*":
    #     answer = num1 * num2
    # elif operator == "/":
    #     try:
    #         answer = num1 / num2
    #     except ZeroDivisionError:
    #         result_label.config(text="You just divided by zero!")
    #         return
    #     except:
    #         result_label.config(text="Other Errors!")

    # # If we encounter a new operator
    # else:
    #     result_label.config(text="Invalid Operator!")

    # result_label.config(text=f'Result: {answer}')


m = tkinter.Tk()
m.title("Calculator")
m.geometry("500x200")
m.configure(bg="lightblue")

heading_font = font.Font(size=20, weight="bold")
result_font = font.Font(size=18)

# Create and place the widgets
entry = tkinter.Entry(m, width=30, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=5)

calculate_button = tkinter.Button(m, text="Calculate", command=calculate, bg="darkblue", fg="white", font=heading_font)
calculate_button.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

result_label = tkinter.Label(m, text="Result: ", bg="lightblue", font=result_font)
result_label.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

m.mainloop()


