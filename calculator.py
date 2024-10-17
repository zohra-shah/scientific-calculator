{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNPgc/T8b5KKIWsrFPLJ1Ij",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/zohra-shah/scientific-calculator/blob/main/calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KeNucI8Z2Nv3"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "import sympy as sp\n",
        "\n",
        "# Function to plot a mathematical expression\n",
        "def plot_function(expr, var, xmin, xmax):\n",
        "    x = sp.Symbol(var)\n",
        "    f = sp.lambdify(x, expr, modules=['numpy'])\n",
        "    X = np.linspace(xmin, xmax, 500)\n",
        "    Y = f(X)\n",
        "    plt.figure(figsize=(8, 6))\n",
        "    plt.plot(X, Y, label=str(expr))\n",
        "    plt.xlabel(var)\n",
        "    plt.ylabel('y')\n",
        "    plt.title('Plot of ' + str(expr))\n",
        "    plt.grid(True)\n",
        "    plt.legend()\n",
        "    st.pyplot(plt)\n",
        "\n",
        "# Main Streamlit application\n",
        "def main():\n",
        "    st.title('Scientific Calculator')\n",
        "\n",
        "    # Input expression\n",
        "    expression = st.text_input('Enter a mathematical expression:', 'sin(x)/x')\n",
        "\n",
        "    # Variable symbol\n",
        "    var_symbol = st.text_input('Variable symbol (e.g., x):', 'x')\n",
        "\n",
        "    # Range for plotting\n",
        "    xmin = st.number_input('Min value for x:', value=-10.0)\n",
        "    xmax = st.number_input('Max value for x:', value=10.0)\n",
        "\n",
        "    # Plot button\n",
        "    if st.button('Plot'):\n",
        "        try:\n",
        "            x = sp.Symbol(var_symbol)\n",
        "            expr = sp.sympify(expression)\n",
        "            plot_function(expr, var_symbol, xmin, xmax)\n",
        "        except Exception as e:\n",
        "            st.error(f'Error: {e}')\n",
        "\n",
        "    # Calculation example\n",
        "    st.subheader('Calculation Example')\n",
        "    example_expr = sp.sin(x) / x\n",
        "    example_result = sp.N(example_expr.subs(x, 1))\n",
        "    st.write(f'Example: sin(x)/x evaluated at x=1 is {example_result}')\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()\n"
      ]
    }
  ]
}