{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMCME49WJRWbzEWIrtYkIi+",
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
        "<a href=\"https://colab.research.google.com/github/zohra-shah/scientific-calculator/blob/main/cancer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "\n",
        "# Function to calculate breast cancer risk using the Gail Model\n",
        "def breast_cancer_risk(age, family_history, age_first_child, num_biopsies, race):\n",
        "    # Base risk calculation (placeholder values; in practice, use real statistical data)\n",
        "    base_risk = 0.012  # Base risk for a 30-year-old\n",
        "\n",
        "    # Adjust risk based on age\n",
        "    if age < 30:\n",
        "        return 0.0  # No risk below 30\n",
        "    elif age < 40:\n",
        "        base_risk += 0.01\n",
        "    elif age < 50:\n",
        "        base_risk += 0.02\n",
        "    elif age < 60:\n",
        "        base_risk += 0.03\n",
        "    else:\n",
        "        base_risk += 0.04\n",
        "\n",
        "    # Adjust for family history\n",
        "    if family_history:\n",
        "        base_risk += 0.05\n",
        "\n",
        "    # Adjust for age at first childbirth\n",
        "    if age_first_child > 30:\n",
        "        base_risk += 0.02\n",
        "\n",
        "    # Adjust for number of biopsies\n",
        "    base_risk += num_biopsies * 0.01\n",
        "\n",
        "    # Adjust for race (simplified)\n",
        "    if race.lower() == 'black':\n",
        "        base_risk += 0.01\n",
        "\n",
        "    return round(base_risk, 4)\n",
        "\n",
        "# Example usage\n",
        "age = 35\n",
        "family_history = True\n",
        "age_first_child = 32\n",
        "num_biopsies = 1\n",
        "race = 'white'\n",
        "\n",
        "risk = breast_cancer_risk(age, family_history, age_first_child, num_biopsies, race)\n",
        "print(f\"The estimated 5-year risk of breast cancer is: {risk * 100}%\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9nJwfB3c4Ts1",
        "outputId": "80eb6e8e-df94-4b52-a142-34a6af20575a"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The estimated 5-year risk of breast cancer is: 10.2%\n"
          ]
        }
      ]
    }
  ]
}