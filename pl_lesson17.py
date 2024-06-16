# Calculator Program
# The calculator must be able to perform addition, subtraction, multiplication and division.
# The calculator take in a continuous string of inputs from the user. The inputs will include either two numbers and an operator. An example of the input is "5 + 10" or "3 * 6".
# The operators will only be +, -, * or /.
# The calculator program will then perform the calculation and print out the result to the user.
import tkinter

def calculate():
    while True:
        # maths = input("Please write: ") # "5 + 10"
        maths = entry.get()

        if maths == "q":
            break

        numbers = maths.split()

        # Check if the user input is valid
        if len(numbers) != 3:
            # print("Invalid input")
            result_label.config(text="Invalid Input")
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
            result_label.config(text="error!")

        result_label.config(text=f'Result: {answer}')


m = tkinter.Tk()
m.title("Calculator")
m.geometry("800x800")

# Create and place the widgets
entry = tkinter.Entry(m, width=30)
entry.grid(row=0, column=0, columnspan=4)

calculate_button = tkinter.Button(m, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=4)

result_label = tkinter.Label(m, text="Result: ")
result_label.grid(row=2, column=0, columnspan=4)

m.mainloop()


