# First, install the required libraries in your terminal or a requirements.txt file
# pip install streamlit numpy matplotlib

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

streamlit
numpy
matplotlib


# Scientific Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    return np.sqrt(a)

# Function for plotting
def plot_function(expr, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = eval(expr)
    plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.title(f'Plot of {expr}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.show()

# Streamlit UI
st.title("Scientific and Graphic Calculator")

# Scientific Calculator
st.header("Scientific Calculator")
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root"])
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Power":
        result = power(num1, num2)

    st.write(f"Result: {result}")

elif operation == "Square Root":
    num = st.number_input("Enter a number", value=0.0)
    if num >= 0:
        result = sqrt(num)
        st.write(f"Square Root: {result}")
    else:
        st.write("Error: Cannot compute square root of a negative number.")

# Plotting
st.header("Function Plotter")
expr = st.text_input("Enter a function of x (e.g., x**2, np.sin(x), np.log(x+1))", "x**2")
x_min = st.number_input("Minimum x value", value=-10.0)
x_max = st.number_input("Maximum x value", value=10.0)

if st.button("Plot"):
    if x_min < x_max:
        plot_function(expr, (x_min, x_max))
    else:
        st.write("Error: Minimum x value must be less than maximum x value.")
