{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Chapter06_03",
      "provenance": [],
      "authorship_tag": "ABX9TyPpjWD50NfOJpk7B3JK2oLH"
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
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ONpAovRYNmRA",
        "outputId": "0e910387-80a2-4890-9100-f5333fc6e1bb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "홍길동 95\n",
            "이순신 77\n",
            "이순신 홍길동 "
          ]
        }
      ],
      "source": [
        "n = int(input())\n",
        "\n",
        "value = [ list(input().split()) for _ in range(n)] #값과 숫자를 리스트 형식으로 받기\n",
        "\n",
        "\n",
        "value.sort(key = lambda x : x[1]) #람다식을 사용하여 내림차순 정렬 , key-value부분에서 value부분만 추출\n",
        "\n",
        "for i in value: #value 데이터에서 값 추출\n",
        "    print(i[0], end = ' ')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "wugFCMebOVg3"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}