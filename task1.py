from tkinter import *

# Initialize the main window
root = Tk()
root.title("Simple Calculator")

# Create an entry widget for user input
input = Entry(root, width=50, borderwidth=5)
input.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

# Initialize global variables
fnum = None
math_operation = None

# Function to handle number button clicks
def click(num):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(num))

# Function to handle addition
def add():
    global fnum
    global math_operation
    math_operation = "addition"
    fnum = int(input.get())
    input.delete(0, END)

# Function to handle subtraction
def subtract():
    global fnum
    global math_operation
    math_operation = "subtraction"
    fnum = int(input.get())
    input.delete(0, END)

# Function to handle multiplication
def multiply():
    global fnum
    global math_operation
    math_operation = "multiplication"
    fnum = int(input.get())
    input.delete(0, END)

# Function to handle division
def divide():
    global fnum
    global math_operation
    math_operation = "division"
    fnum = int(input.get())
    input.delete(0, END)

# Function to clear the input field
def clear():
    input.delete(0, END)

# Function to evaluate the expression
def equal():
    snum = int(input.get())
    input.delete(0, END)
    
    if math_operation == "addition":
        result = fnum + snum
    elif math_operation == "subtraction":
        result = fnum - snum
    elif math_operation == "multiplication":
        result = fnum * snum
    elif math_operation == "division":
        if snum == 0:
            result = "Error"  # Avoid division by zero
        else:
            result = fnum / snum
    
    input.insert(0, result)

# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=add)
button_subtract = Button(root, text="-", padx=41, pady=20, command=subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=divide)
button_clear = Button(root, text="AC", padx=36, pady=20, command=clear)
button_equal = Button(root, text="=", padx=91, pady=20, command=equal)

# Place buttons on the grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_add.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)

button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=2)

# Run the main loop
root.mainloop()
