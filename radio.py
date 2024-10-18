{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOT8JX3of8qTWiAnuN3LeF6",
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
        "<a href=\"https://colab.research.google.com/github/zohra-shah/scientific-calculator/blob/main/radio.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Import necessary libraries\n",
        "import pandas as pd\n",
        "\n",
        "# Function to calculate equivalent dose\n",
        "def calculate_equivalent_dose(dose, quality_factor):\n",
        "    return dose * quality_factor\n",
        "\n",
        "# Function to calculate effective dose\n",
        "def calculate_effective_dose(equivalent_dose, tissue_weighting_factor):\n",
        "    return equivalent_dose * tissue_weighting_factor\n",
        "\n",
        "# Function to create a user interface\n",
        "def radiological_calculator():\n",
        "    print(\"Welcome to the Radiological Calculator!\")\n",
        "\n",
        "    # Input for Dose (in Gray)\n",
        "    dose = float(input(\"Enter Dose (in Gray): \"))\n",
        "\n",
        "    # Input for Quality Factor\n",
        "    quality_factor = float(input(\"Enter Quality Factor: \"))\n",
        "\n",
        "    # Input for Tissue Weighting Factor\n",
        "    tissue_weighting_factor = float(input(\"Enter Tissue Weighting Factor: \"))\n",
        "\n",
        "    # Calculations\n",
        "    equivalent_dose = calculate_equivalent_dose(dose, quality_factor)\n",
        "    effective_dose = calculate_effective_dose(equivalent_dose, tissue_weighting_factor)\n",
        "\n",
        "    # Display results\n",
        "    print(f\"\\nEquivalent Dose: {equivalent_dose:.2f} Sv\")\n",
        "    print(f\"Effective Dose: {effective_dose:.2f} Sv\")\n",
        "\n",
        "# Run the calculator\n",
        "radiological_calculator()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pQRnrNZm1I6z",
        "outputId": "c760347e-654c-4a18-c0ec-851ad666b361"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to the Radiological Calculator!\n",
            "Enter Dose (in Gray): 35\n",
            "Enter Quality Factor: 56\n",
            "Enter Tissue Weighting Factor: 76\n",
            "\n",
            "Equivalent Dose: 1960.00 Sv\n",
            "Effective Dose: 148960.00 Sv\n"
          ]
        }
      ]
    }
  ]
}