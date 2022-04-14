{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "011~20",
      "provenance": [],
      "authorship_tag": "ABX9TyNUljKCKU1WvIGR3lvWxM3X",
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
        "<a href=\"https://colab.research.google.com/github/qsdcfd/Year-dream/blob/TIL/Theory/Python/Questions/011~20.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DvIMnwtCsBVZ",
        "outputId": "0b8cd439-d52f-401e-c2dc-16d460a98d30"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "500000\n"
          ]
        }
      ],
      "source": [
        "#011 변수를 사용하기\n",
        "\n",
        "#삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.\n",
        "\n",
        "삼성전자 = 50000\n",
        "주식 = 10\n",
        "\n",
        "평가금액 = 삼성전자 * 주식\n",
        "print(평가금액)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#012 변수 사용하기\n",
        "#다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.\n",
        "\n",
        "시가총액 = 298000000000000\n",
        "현재가 = 50000\n",
        "PER = 15.79\n",
        "print(시가총액, type(시가총액))\n",
        "print(현재가, type(현재가))\n",
        "print(PER, type(PER))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "96riuuUjtCsE",
        "outputId": "55214fc4-1af3-43a0-e3db-89667b1e9ee3"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "298000000000000 <class 'int'>\n",
            "50000 <class 'int'>\n",
            "15.79 <class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#013문자열 출력\n",
        "#변수 s와 t에는 각각 문자열이 바인딩\n",
        "\n",
        "s = \"hello\"\n",
        "t = \"python\"\n",
        "\n",
        "print(s + \"!\" , t)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r9BjvcumtQ7w",
        "outputId": "3e8c5a79-292a-4f66-bcf8-a1d42af55ec2"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello! python\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#014파이썬을 이용한 값 계산\n",
        "\n",
        "print(2 + 2*3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4upDHrNYte5X",
        "outputId": "f9c3ce16-a5e4-44c0-ca83-4e29c4810c5f"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#015 type함수\n",
        "\n",
        "a= \"132\"\n",
        "print(type(a))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lUa4HLvVtnbM",
        "outputId": "eb985922-1567-40cd-e3f3-4c579bdfd1b9"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#016 문자열을 정수로 반환\n",
        "\n",
        "num_str = \"720\"\n",
        "number = int(num_str)\n",
        "\n",
        "print(type(number))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KWjwFdwHtznh",
        "outputId": "333d8a26-aab1-4a0c-89be-56abf47a8807"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#017 정수를 문자열로 변환\n",
        "\n",
        "num = 100\n",
        "\n",
        "num_st = str(num)\n",
        "\n",
        "print(type(num_st))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AleGTO2UuAer",
        "outputId": "d589427b-6862-410a-e903-11e53cb518ed"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#018 문자열을 실수로 변환\n",
        "\n",
        "fig = \"15.79\"\n",
        "float1 = float(fig)\n",
        "\n",
        "print(type(float1))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p7tWjl3euJBO",
        "outputId": "0549e009-00fd-4be4-fbce-663ba2addc72"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#019 문자열을 정수로 변환\n",
        "\n",
        "year = \"2020\"\n",
        "year_1 = int(year)\n",
        "\n",
        "print(year_1 - 1)\n",
        "print(year_1 - 2)\n",
        "print(year_1 - 3)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3DbmH9HnuT_s",
        "outputId": "1a8a4537-bf5d-42b2-a8d7-12107e225381"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2019\n",
            "2018\n",
            "2017\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#020 파이썬 계산\n",
        "\n",
        "month = 48584 \n",
        "money = month * 36\n",
        "print(\"총 금액:\", money)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q4VkzRN7uiuL",
        "outputId": "b0362128-08af-44f6-b318-2e421c16b8ec"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "총 금액: 1749024\n"
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
        "id": "ckyxE5AXuu2I"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}