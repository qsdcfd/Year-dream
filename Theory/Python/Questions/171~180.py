{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "171~180",
      "provenance": [],
      "authorship_tag": "ABX9TyNxsOj5k2mNrR03FvXctdsJ"
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
      "execution_count": 4,
      "metadata": {
        "id": "Vv7sA3ImExDs",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "941f9835-2fee-4be6-84e6-a59af2b1da5f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "32100\n",
            "32150\n",
            "32000\n",
            "32500\n"
          ]
        }
      ],
      "source": [
        "#171: 아래와 같이 리스트 데이터를 출력하라(for, range문 사용)\n",
        "\n",
        "price_list = [32100, 32150, 32000, 32500]\n",
        "\n",
        "for i in range(len(price_list)):\n",
        "    print(price_list[i])"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#172 리스트 데이터 출력, for , range문 출력\n",
        "\n",
        "price_list = [32100, 32150, 32000, 32500]\n",
        "\n",
        "for i in range(len(price_list)):\n",
        "    print(i, price_list[i])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5yU1jYi0kB1H",
        "outputId": "7e4bfb2c-d5d0-4dcb-e8e5-841f59ba9022"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 32100\n",
            "1 32150\n",
            "2 32000\n",
            "3 32500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#리스트의 데이터를 출력하라, for문과 range문 사용하라\n",
        "\n",
        "price_list = [32100, 32150, 32000, 32500]\n",
        "\n",
        "for i in range(len(price_list)):\n",
        "    print(3-i,price_list[i])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4NZPuM9YldGJ",
        "outputId": "e343c1f6-9832-4570-cfaa-cbf4d0a1abed"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 32100\n",
            "2 32150\n",
            "1 32000\n",
            "0 32500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#174 리스트 데이터 출력, for , range문 출력\n",
        "\n",
        "price_list = [32100, 32150, 32000, 32500]\n",
        "\n",
        "for i in range(1,4):\n",
        "    print(100+10*(i-1), price_list[i])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C179QM7ZkoXH",
        "outputId": "fbaf04a8-6100-499a-f318-b6fdd54c992b"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100 32150\n",
            "110 32000\n",
            "120 32500\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#175 조건에 맞게 출력하라\n",
        "\n",
        "my_list = [\"가\", \"나\", \"다\", \"라\"]\n",
        "\n",
        "for i in range(3):\n",
        "    print(my_list[i-4], my_list[i-3])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jfwW7rWllENi",
        "outputId": "10bdf57e-71a7-4e36-a23f-bbfff4776e7f"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "가 나\n",
            "나 다\n",
            "다 라\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#176 조건메 맞게 출력\n",
        "my_list = [\"가\", \"나\", \"다\", \"라\", \"마\"]\n",
        "\n",
        "for i in range(3):\n",
        "    print(my_list[i-5],my_list[i-4],my_list[i-3])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bG_JBg_PmG7m",
        "outputId": "41bf7f3b-b7a3-4b9f-9eea-63fad85c476d"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "가 나 다\n",
            "나 다 라\n",
            "다 라 마\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#177 반복문과 range함수를 사용하여 my_list출력\n",
        "my_list = [\"가\", \"나\", \"다\", \"라\"]\n",
        "for i in range(len(my_list) - 1, 0, -1):\n",
        "    print(my_list[i], my_list[i-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iKTq5_Xrm0ZM",
        "outputId": "4dca26ea-bf1e-47e4-c268-27f5500affeb"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "라 다\n",
            "다 나\n",
            "나 가\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#178 자신과 우측값과 차분값을 화면에 출력\n",
        "my_list = [100, 200, 400, 800]\n",
        "\n",
        "for i in range(3):\n",
        "    print(my_list[i])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aToxIH8xnLu9",
        "outputId": "a9e22e4c-8331-4a9e-8008-0f3df0be5d8b"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100\n",
            "200\n",
            "400\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#179 6일간의 종가 데이터가 저장되어잇는 3일 이동 평균 계산하고 화면 출력\n",
        "\n",
        "my_list = [100, 200, 400, 800, 1000, 1300]\n",
        "\n",
        "for i in range(1,len(my_list)-1):\n",
        "    print(abs(my_list[i-1] + my_list[i] + my_list[i+1])/3)\n",
        "    "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qqHm-SUbnfwP",
        "outputId": "211bd68a-f147-4d2f-f713-8fe9b7e23c61"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "233.33333333333334\n",
            "466.6666666666667\n",
            "733.3333333333334\n",
            "1033.3333333333333\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#180 \n",
        "#리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, \n",
        "#low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.\n",
        "\n",
        "low_prices  = [100, 200, 400, 800, 1000]\n",
        "high_prices = [150, 300, 430, 880, 1000]\n",
        "\n",
        "volatility = []\n",
        "\n",
        "for i in range(len(low_prices)):\n",
        "    volatility.append(high_prices[i]-low_prices[i])"
      ],
      "metadata": {
        "id": "xTng7yOrqYfG"
      },
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "ErbfGaEYqxpz"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}