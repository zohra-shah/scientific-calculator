{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMwuaVK1M4Ggv8EURhWh2QC",
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
        "<a href=\"https://colab.research.google.com/github/zohra-shah/scientific-calculator/blob/main/cal.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import math\n",
        "\n",
        "# Title of the app\n",
        "st.title(\"Scientific Calculator\")\n",
        "\n",
        "# Sidebar for selecting operation\n",
        "operation = st.sidebar.selectbox(\n",
        "    \"Select an operation\",\n",
        "    (\"Addition\", \"Subtraction\", \"Multiplication\", \"Division\",\n",
        "     \"Power\", \"Square Root\", \"Trigonometric Functions\", \"Logarithm\")\n",
        ")\n",
        "\n",
        "# Input fields\n",
        "num1 = st.number_input(\"Enter first number\", value=0.0)\n",
        "num2 = st.number_input(\"Enter second number\", value=0.0)\n",
        "\n",
        "if operation == \"Addition\":\n",
        "    result = num1 + num2\n",
        "elif operation == \"Subtraction\":\n",
        "    result = num1 - num2\n",
        "elif operation == \"Multiplication\":\n",
        "    result = num1 * num2\n",
        "elif operation == \"Division\":\n",
        "    result = num1 / num2 if num2 != 0 else \"Error: Division by zero\"\n",
        "elif operation == \"Power\":\n",
        "    result = num1 ** num2\n",
        "elif operation == \"Square Root\":\n",
        "    result = math.sqrt(num1) if num1 >= 0 else \"Error: Negative input\"\n",
        "elif operation == \"Trigonometric Functions\":\n",
        "    angle = st.number_input(\"Enter angle in degrees\", value=0.0)\n",
        "    radian = math.radians(angle)\n",
        "    result = {\n",
        "        \"sin\": math.sin(radian),\n",
        "        \"cos\": math.cos(radian),\n",
        "        \"tan\": math.tan(radian)\n",
        "    }\n",
        "elif operation == \"Logarithm\":\n",
        "    base = st.number_input(\"Enter base (default is e)\", value=math.e)\n",
        "    result = math.log(num1, base) if num1 > 0 else \"Error: Logarithm of non-positive number\"\n",
        "\n",
        "# Display the result\n",
        "st.write(\"Result:\", result)\n"
      ],
      "metadata": {
        "id": "4rdjvoDWUCAa"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}