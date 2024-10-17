import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Function to plot a mathematical expression
def plot_function(expr, var, xmin, xmax):
    x = sp.Symbol(var)
    f = sp.lambdify(x, expr, modules=['numpy'])
    X = np.linspace(xmin, xmax, 500)
    Y = f(X)
    plt.figure(figsize=(8, 6))
    plt.plot(X, Y, label=str(expr))
    plt.xlabel(var)
    plt.ylabel('y')
    plt.title('Plot of ' + str(expr))
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

# Main Streamlit application
def main():
    st.title('Scientific Calculator')

    # Input expression
    expression = st.text_input('Enter a mathematical expression:', 'sin(x)/x')

    # Variable symbol
    var_symbol = st.text_input('Variable symbol (e.g., x):', 'x')

    # Range for plotting
    xmin = st.number_input('Min value for x:', value=-10.0)
    xmax = st.number_input('Max value for x:', value=10.0)

    # Plot button
    if st.button('Plot'):
        try:
            x = sp.Symbol(var_symbol)
            expr = sp.sympify(expression)
            plot_function(expr, var_symbol, xmin, xmax)
        except Exception as e:
            st.error(f'Error: {e}')

    # Calculation example
    st.subheader('Calculation Example')
    example_expr = sp.sin(x) / x
    example_result = sp.N(example_expr.subs(x, 1))
    st.write(f'Example: sin(x)/x evaluated at x=1 is {example_result}')

if __name__ == '__main__':
    main()
