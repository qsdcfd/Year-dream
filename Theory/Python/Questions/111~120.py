{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "111~120",
      "provenance": [],
      "authorship_tag": "ABX9TyNIcQZ2ioc4TciGP/xwGLhC"
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
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FEVoZbIdnRri",
        "outputId": "40bd5544-288e-4ceb-adcf-5f5b9a239a7b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "안녕하세요\n",
            "안녕하세요안녕하세요\n"
          ]
        }
      ],
      "source": [
        "#111: 사용자로부터 입력받은 문자열을 두 번 출력하라\n",
        "n = input()\n",
        "print(n*2)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#112: 사용자로부터 하나의 숫자를 입력받고 입력 받은 숫자에 10을 더해 출력\n",
        "\n",
        "fig = int(input(\"숫자를 입력하세요:\"))\n",
        "\n",
        "print(fig + 10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "52ndEalowsLt",
        "outputId": "605ab865-8f9d-48cd-924c-cd02e02c2c07"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "숫자를 입력하세요:30\n",
            "40\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#113: 사용자로부터 하나의 숫자를 입력받고 짝수/홀수를 판별하라\n",
        "\n",
        "even1 = int(input())\n",
        "\n",
        "if even1 % 2 ==0:\n",
        "    print(\"짝수\")\n",
        "\n",
        "else:\n",
        "    print(\"홀수\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BVjDdUvhw-6i",
        "outputId": "197237cf-886e-41d0-e935-479bbb1613d8"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30\n",
            "짝수\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#114: 입력값에 20을 더한 값을 출력하라 20을 더한 값이 255를 초과하는 경우 255출력\n",
        "\n",
        "figure = int(input(\"입력값:\"))\n",
        "\n",
        "sum1 = figure + 20\n",
        "\n",
        "if sum1 < 255:\n",
        "    print(\"출력값:\", sum1)\n",
        "else:\n",
        "    print(\"출력값:\", 255)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sZ5-NqZ5xWdv",
        "outputId": "e34a0adb-c98d-4ac6-8c72-1f1e05258ed4"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "입력값:240\n",
            "255\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#115: 입력값을 받은 후에 해당 값의 20을 뺀 값을 출력하라. 출력값의 범위는 0~255이다.\n",
        "\n",
        "figu = int(input(\"입력값:\"))\n",
        "\n",
        "sum2 = figu - 20\n",
        "\n",
        "if sum2 > 255:\n",
        "    print(\"출력값:\" , 255)\n",
        "elif sum2 <0:\n",
        "    print(\"출력값:\", 0)\n",
        "else: \n",
        "    print(\"출력값:\", sum2)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7mXppnsmxxum",
        "outputId": "fbdd63ce-2c61-491e-ccc9-520a97a8d4c0"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "입력값:14\n",
            "출력값: 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#116: 사용자로부터 입력 받은 시간이 정각인지 판별\n",
        "\n",
        "time1 = input(\"현재시간:\")\n",
        "\n",
        "if time1[-2:] == '00':\n",
        "    print(\"정각 입니다.\")\n",
        "else:\n",
        "    print(\"정각이 아닙니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GMbk2whNyf4I",
        "outputId": "e89686b9-7c40-45e3-952e-8f39eb25e8f2"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "현재시간:03:34\n",
            "정각이 아닙니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#117: 입력받은 단어가 아래 fruit리스트에 포함되어있는지 확인해라\n",
        "\n",
        "fruit = [\"사과\", \"포도\", \"홍시\"]\n",
        "\n",
        "fruits = input(\"좋아하는 과일은?\" )\n",
        "\n",
        "if fruits in fruit:\n",
        "    print(\"정답입니다.\")\n",
        "else:\n",
        "    print(\"오답입니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bbX5c1F2zVU_",
        "outputId": "8ea407a9-2ed5-4549-f784-0d803b98055d"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "좋아하는 과일은?바나나\n",
            "오답입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#118: 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이면\n",
        "\n",
        "warn_investment_list = [\"Microsoft\", \"Google\", \"Naver\", \"Kakao\", \"SAMSUNG\", \"LG\"]\n",
        "\n",
        "warn1 = input(\"종목명:\" )\n",
        "\n",
        "if warn1 in warn_investment_list:\n",
        "    print(\"투자 경고 종목입니다.\")\n",
        "\n",
        "else:\n",
        "    print(\"투자 경고 종목이 아닙니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J873euWJ3Vi6",
        "outputId": "7a585e79-5e04-466c-b84f-6227a14c097e"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "종목명:SK\n",
            "투자 경고 종목이 아닙니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#119: fruit가 딕셔너리로 정의되어있는데 사용자가 입력한 값이 포함되어 있다면 \"정답입니다\" 그렇지 않다면 \"오답입니다.\"\n",
        "\n",
        "fruit = {\"봄\" : \"딸기\", \"여름\" : \"토마토\", \"가을\" : \"사과\"}\n",
        "\n",
        "fruit1 = input(\"제가 좋아하는 계절은:\" )\n",
        "\n",
        "if fruit1 in fruit:\n",
        "    print(\"정답입니다.\")\n",
        "else:\n",
        "    print(\"오답입니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EVW9tA1h3yUM",
        "outputId": "ed33e934-a209-4518-9b44-2ead2ce5dba2"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "제가 좋아하는 계절은:봄\n",
            "정답입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#120: 사용자가 입력한 값이 딕셔너리 값에 포함되어있다면 정답 그렇지 않다면 오답입니다.\n",
        "\n",
        "fruit = {\"봄\" : \"딸기\", \"여름\" : \"토마토\", \"가을\" : \"사과\"}\n",
        "\n",
        "fruit1 = input(\"제가 좋아하는 과일은:\" )\n",
        "\n",
        "if fruit1 in fruit:\n",
        "    print(\"정답입니다.\")\n",
        "else:\n",
        "    print(\"오답입니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xJ576s-h4a7t",
        "outputId": "b3a175b2-0113-489b-db99-6f14a4922fdd"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "제가 좋아하는 과일은:한라봉\n",
            "오답입니다.\n"
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
        "id": "WI-glqV542md"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}