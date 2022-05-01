{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "chapter02_04",
      "provenance": [],
      "authorship_tag": "ABX9TyMrj0oGwa6e+b2kaH95vf8k"
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
        "id": "v6SbZQJ6aiXN",
        "outputId": "d0b1d4ef-cc76-47c2-ff19-fc7842d73df4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "17 4\n",
            "3\n"
          ]
        }
      ],
      "source": [
        "N, K = map(int,input().split())\n",
        "\n",
        "result = 0\n",
        "\n",
        "while N !=1:\n",
        "    if N % K != 0:\n",
        "        N = N-1\n",
        "        result +=1\n",
        "    else:\n",
        "        N = N/K\n",
        "        result +=1\n",
        "\n",
        "print(result)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "__kX-dzPcEXa"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}