{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "\bGCD_Algorithm",
      "provenance": [],
      "authorship_tag": "ABX9TyPFOf/geg8kocyKTLr4xgYB"
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
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "roeoz1iHbFAL",
        "outputId": "81e0974d-e104-44cc-feba-2f4907b7d78d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "최대공약수: 5\n"
          ]
        }
      ],
      "source": [
        "## 뺄셈 풀이\n",
        "def gcd_sub(a,b):\n",
        "    while a != 0 and b != 0:\n",
        "        if a>b:\n",
        "            a = a-b\n",
        "        else:\n",
        "            b = b-a\n",
        "\n",
        "    return a+ b\n",
        "\n",
        "results = gcd_sub(5,20)\n",
        "print(\"최대공약수:\", results)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "##나눗셈 풀이\n",
        "def gcd_mod(c,d):\n",
        "    while c != 0 and d != 0:\n",
        "        if c>d:\n",
        "            c = c/d\n",
        "        else:\n",
        "            d = d/c\n",
        "    return c + d\n",
        "\n",
        "#res = gcd_mod(2,6)\n",
        "#print(\"최대공약수:\", res)"
      ],
      "metadata": {
        "id": "5U-cGZr2exrg"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "##재귀 함수\n",
        "def gcd_rec(p, q):\n",
        "    if q == 0:\n",
        "        return p\n",
        "    else:\n",
        "        return gcd_rec(q, p % q)\n",
        "\n",
        "result = gcd_rec(10, 12)\n",
        "print('최대공약수:',result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ph4S38-Wdb0K",
        "outputId": "5fd08d65-0b5b-4164-985e-937c65853c18"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "최대공약수: 2\n"
          ]
        }
      ]
    }
  ]
}