import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="black")

# Style configurations
label_font = ("Arial", 12, "bold")
button_font = ("Arial", 12, "bold")

label_fg = "white"
entry_bg = "#333333"
entry_fg = "white"
button_bg = "#555555"
button_fg = "white"

# Create input fields
entry_num1 = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=label_font, borderwidth=3)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

entry_num2 = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=label_font, borderwidth=3)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Create labels
tk.Label(root, text="Enter first number:", bg="black", fg=label_fg, font=label_font).grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Enter second number:", bg="black", fg=label_fg, font=label_font).grid(row=1, column=0, padx=10, pady=10)

# Create dropdown for operations
operation_var = tk.StringVar(root)
operation_var.set("+")  # default value
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.config(bg=button_bg, fg=button_fg, font=label_font, borderwidth=3)
operation_menu.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Select operation:", bg="black", fg=label_fg, font=label_font).grid(row=2, column=0, padx=10, pady=10)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate, bg=button_bg, fg=button_fg, font=button_font, borderwidth=3)
calculate_button.grid(row=3, column=1, padx=10, pady=10)

# Create label to display the result
result_label = tk.Label(root, text="Result: ", bg="black", fg=label_fg, font=label_font)
result_label.grid(row=4, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
