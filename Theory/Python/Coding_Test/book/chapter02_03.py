{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "chapter02_03",
      "provenance": [],
      "authorship_tag": "ABX9TyNnm72AVDfzh4fQzAemb+pI"
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
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4cJt-AWqsHaY",
        "outputId": "cc239fde-62ae-41b7-a8ff-e67dde1c17b5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 3\n",
            "7 3 8\n",
            "3 3 2\n",
            "2\n"
          ]
        }
      ],
      "source": [
        "#행렬에서 최종행렬의 최솟값 카드 뽑기\n",
        "\n",
        "n,m = map(int,input().split())# n x m 행렬 만든다\n",
        "\n",
        "for i in range(n):\n",
        "    row1 = map(int,input().split())\n",
        "    \n",
        "    min1 = min(row1)\n",
        "    \n",
        "\n",
        "print(min1)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "SBo9PGcjtQ1Z"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}