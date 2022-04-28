{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "chapter02_01",
      "provenance": [],
      "authorship_tag": "ABX9TyOBM+ZDm4UVkX98HJNuQbXo"
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
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QA49UndQ6QUf",
        "outputId": "91aae37b-97b5-4aeb-ecf6-f9a430d9218f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 2, 1, 1]\n",
            "6\n"
          ]
        }
      ],
      "source": [
        "#거스름돈, 동전 최소 갯수\n",
        "\n",
        "money = [500,100,50,10]\n",
        "\n",
        "pay = 1260\n",
        "count = []\n",
        "\n",
        "for i in money:\n",
        "    \n",
        "    count.append(pay //i)\n",
        "    pay %= i\n",
        "\n",
        "print(count)\n",
        "print(sum(count))\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "f0r4hyZP7H0v"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}