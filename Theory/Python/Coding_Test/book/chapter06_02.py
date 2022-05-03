{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "chapter06_02",
      "provenance": [],
      "authorship_tag": "ABX9TyNEzvSrK2TDjSrnQtkU5Z8M"
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
      "source": [
        "N=int(input()) #숫자 갯수\n",
        "nums=[int(input()) for i in range(N)] #리스트 컴프리헨션, 넣을 숫자 (15,27,12)\n",
        "nums.sort(reverse=True) #리버스\n",
        "\n",
        "print(nums)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jP8fKOwRSnyQ",
        "outputId": "68c7e144-5f81-4b3c-aa24-0d9378910688"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "15\n",
            "27\n",
            "2\n",
            "[27, 15, 2]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input())\n",
        "\n",
        "values1 = []\n",
        "for i in range(N):\n",
        "    numbers = int(input())\n",
        "    values1.append(numbers)\n",
        "    values1.sort(reverse=True)\n",
        "print(values1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wgpV5QuMUxpf",
        "outputId": "db8430ee-54e5-4307-bd3a-6a7f5edfd7de"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "15\n",
            "27\n",
            "12\n",
            "[27, 15, 12]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "lZC8FQqDVsql"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}