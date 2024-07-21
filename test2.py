import tkinter as tk
from tkinter import font

def calculate():
    maths = entry.get()

    if maths.lower() == "q":
        m.quit()
        return

    numbers = maths.split()

    # Check if the user input is valid
    if len(numbers) != 3:
        result_label.config(text="Invalid Input")
        return

    num1, operator, num2 = numbers

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        result_label.config(text="Invalid Input")
        return

    # Perform the calculation based on the operator (+, -, *, /)
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        try:
            answer = num1 / num2
        except ZeroDivisionError:
            result_label.config(text="Division by Zero Error")
            return
    else:
        result_label.config(text="Invalid Operator")
        return

    result_label.config(text=f'Result: {answer}')

# Create the main window
m = tk.Tk()
m.title("Calculator")
m.geometry("400x200")
m.configure(bg="#f0f0f0")

# Custom fonts
title_font = font.Font(family="Helvetica", size=16, weight="bold")
button_font = font.Font(family="Helvetica", size=12)
result_font = font.Font(family="Helvetica", size=14)

# Create and place the widgets
title_label = tk.Label(m, text="Simple Calculator", font=title_font, bg="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=4, pady=10)

entry = tk.Entry(m, width=30, font=result_font)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

calculate_button = tk.Button(m, text="Calculate", command=calculate, font=button_font, bg="#4CAF50", fg="white", padx=10, pady=5)
calculate_button.grid(row=2, column=0, columnspan=4, pady=10)

result_label = tk.Label(m, text="Result: ", font=result_font, bg="#f0f0f0")
result_label.grid(row=3, column=0, columnspan=4, pady=10)

m.mainloop()
