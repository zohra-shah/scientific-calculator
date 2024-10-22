import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator")

# Sidebar for selecting operation
operation = st.sidebar.selectbox(
    "Select an operation",
    ("Addition", "Subtraction", "Multiplication", "Division", 
     "Power", "Square Root", "Trigonometric Functions", "Logarithm")
)

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Initialize result variable
result = None

if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
elif operation == "Power":
    result = num1 ** num2
elif operation == "Square Root":
    result = math.sqrt(num1) if num1 >= 0 else "Error: Negative input"
elif operation == "Trigonometric Functions":
    angle = st.number_input("Enter angle in degrees", value=0.0)
    radian = math.radians(angle)
    result = {
        "sin": math.sin(radian),
        "cos": math.cos(radian),
        "tan": math.tan(radian)
    }
elif operation == "Logarithm":
    base = st.number_input("Enter base (default is e)", value=math.e)
    result = math.log(num1, base) if num1 > 0 else "Error: Logarithm of non-positive number"

# Display the result
if result is not None:
    st.write("Result:", result)
