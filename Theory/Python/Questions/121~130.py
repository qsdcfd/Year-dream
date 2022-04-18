{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "121~130",
      "provenance": [],
      "authorship_tag": "ABX9TyOe/atY3tALBa/PaVf823VY"
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
        "id": "joZoGmX35jQ1",
        "outputId": "4c9499ed-8420-4b12-e109-1d9281342239"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A\n",
            "a\n"
          ]
        }
      ],
      "source": [
        "#121: 문자 한 개를 입력받고 소문자면 대문자로 대문자면 소문자로 변경하라\n",
        "\n",
        "cha = input()\n",
        "\n",
        "if cha.islower():\n",
        "    print(cha.upper())\n",
        "else:\n",
        "    print(cha.lower())\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#122: 사용자로부터 score를 입력받아 학점 출력\n",
        "\n",
        "score1 = input(\"score:\")\n",
        "score2 = int(score1)\n",
        "if score2 > 80:\n",
        "    print(\"grade is A\" )\n",
        "elif score2 > 60:\n",
        "    print(\"grade is B\")\n",
        "elif score2 > 40:\n",
        "    print(\"grade is C\")\n",
        "elif score2 > 20:\n",
        "    print(\"grade is D\")\n",
        "else:\n",
        "    print(\"grade is E\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BpwBs5di6Zfl",
        "outputId": "5a7bf12c-50df-4775-9f49-88ffe5ffff19"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "score:83\n",
            "grade is A\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#123 \n",
        "환율 = {\"달러\": 1167, \n",
        "        \"엔\": 1.096, \n",
        "        \"유로\": 1268, \n",
        "        \"위안\": 171}\n",
        "user = input(\"입력: \")\n",
        "\n",
        "num, currency = user.split()\n",
        "\n",
        "print(float(num) * 환율[currency], \"원\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "682TZ40D7gCm",
        "outputId": "22b64ac2-a690-4244-f729-31729645fb7b"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "입력: 100 달러\n",
            "116700.0 원\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#124: 숫자 3개를 입력하여 가장 큰 값 찾기\n",
        "num1 = input(\"input number1: \")\n",
        "num2 = input(\"input number2: \")\n",
        "num3 = input(\"input number3: \")\n",
        "num1 = int(num1)\n",
        "num2 = int(num2)\n",
        "num3 = int(num3)\n",
        "\n",
        "if num1 >= num2 and num1 >= num3:\n",
        "    print(num1)\n",
        "elif num2 >= num1 and num2 >= num3:\n",
        "    print(num2)\n",
        "else:\n",
        "    print(num3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AGU-A9Ve78ZX",
        "outputId": "25b4f0a7-cbce-49b9-ef80-8294ee5f4d93"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "input number1: 10\n",
            "input number2: 9\n",
            "input number3: 20\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#125\n",
        "number = input(\"휴대전화 번호 입력: \")\n",
        "num = number.split(\"-\")[0]\n",
        "if num == \"011\":\n",
        "    com = \"SKT\"\n",
        "elif num == \"016\":\n",
        "    com = \"KT\"\n",
        "elif num == \"019\":\n",
        "    com = \"LGU\"\n",
        "else:\n",
        "    com = \"알수없음\"\n",
        "print(f\"당신은 {com} 사용자입니다.\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N7pjazRp89Rf",
        "outputId": "5ea56d6e-75b4-4805-bb85-46cbf2eac3e8"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "휴대전화 번호 입력: 010-345-1922\n",
            "당신은 알수없음 사용자입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#126\n",
        "우편번호 = input(\"우편번호: \")\n",
        "우편번호 = 우편번호[:3]\n",
        "if 우편번호 in [\"010\", \"011\", \"012\"]:\n",
        "    print(\"강북구\")\n",
        "elif 우편번호 in [\"014\", \"015\", \"016\"]:\n",
        "    print(\"도봉구\")\n",
        "else:\n",
        "    print(\"노원구\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c3K9VPsN_Dqp",
        "outputId": "3e139a09-fcf5-4e07-f608-c19eeb1867a2"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "우편번호: 01400\n",
            "도봉구\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#127\n",
        "\n",
        "주민번호 = input(\"주민등록번호: \")\n",
        "주민번호 = 주민번호.split(\"-\")[1]\n",
        "if 주민번호[0] == \"1\" or 주민번호[0] == \"3\":\n",
        "    print(\"남자\")\n",
        "else:\n",
        "    print(\"여자\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TTTY7Fj5_OIP",
        "outputId": "9843e35a-2e56-426a-ab5d-62e954263937"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "주민등록번호: 821010-1635210\n",
            "남자\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#128\n",
        "\n",
        "주민번호 = input(\"주민등록번호: \")\n",
        "뒷자리 = 주민번호.split(\"-\")[1]\n",
        "if 0 <= int(뒷자리[1:3]) <= 8:\n",
        "    print(\"서울입니다.\")\n",
        "else:\n",
        "    print(\"서울이 아닙니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V7_vR5ul_1N4",
        "outputId": "8fa66d80-85e8-4de9-b051-f880c7b712c6"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "주민등록번호: 821010-1635210\n",
            "서울이 아닙니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = input(\"주민등록번호: \")\n",
        "계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \\\n",
        "        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \\\n",
        "        int(num[11])* 4 + int(num[12]) * 5\n",
        "계산2 = 11 - (계산1 % 11)\n",
        "계산3 = str(계산2)\n",
        "\n",
        "if num[-1] == 계산3[-1]:\n",
        "    print(\"유효한 주민등록번호입니다.\")\n",
        "else:\n",
        "    print(\"유효하지 않은 주민등록번호입니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CFjX91neAX0T",
        "outputId": "9db07336-3c5a-48a3-b8db-4f21c1b4f3b7"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "주민등록번호: 821010-1635210\n",
            "유효하지 않은 주민등록번호입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "btc = requests.get(\"https://api.bithumb.com/public/ticker/\").json()['data']\n",
        "\n",
        "변동폭 = float(btc['max_price']) - float(btc['min_price'])\n",
        "시가 = float(btc['opening_price'])\n",
        "최고가 = float(btc['max_price'])\n",
        "\n",
        "if (시가+변동폭) > 최고가:\n",
        "    print(\"상승장\")\n",
        "else:\n",
        "    print(\"하락장\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FTaJ9yA5AdXN",
        "outputId": "c11a9069-1e81-41a3-bc47-650a79b2cc0d"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "상승장\n"
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
        "id": "629fQHxRAiuc"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}