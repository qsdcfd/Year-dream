{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "chapter02_02",
      "provenance": [],
      "authorship_tag": "ABX9TyOL1ebyBaLjxB+kDjms3a5N"
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
        "id": "s4j3pK4Phcoz",
        "outputId": "35d65631-b70c-4ded-e203-ebb86697ce5c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 8 3\n",
            "2 4 5 4 6\n",
            "46\n"
          ]
        }
      ],
      "source": [
        "#큰 수의 법칙\n",
        "N,M,K = map(int, input().split()) #배열 숫자 갯수, 총 더하는 횟수, K는 인덱스가 같은 것을 연속성 사용 시 최대 횟수\n",
        "\n",
        "array1 = list(map(int, input().split()))\n",
        "\n",
        "array1.sort()\n",
        "\n",
        "#인덱싱으로 설정하는 이유는, 같은 수여도 인덱싱이 다르면 다른 숫자 취급\n",
        "#최대, 두번째 큰 수라고 보긴 어려울 수도 있다\n",
        "#max함수를 사용하면 안되는 이유\n",
        "\n",
        "first = array1[N-1] \n",
        "second = array1[N-2]\n",
        "\n",
        "sum1 = 0 # first,second의 총 합\n",
        "\n",
        "while True: # 무한 루프 차피 아래에서 조건 맞으면 내보내면 되니끼\n",
        "\n",
        "    for i in range(K):#K번 만큼 더함\n",
        "        if M == 0: #M이 0 이라는 것은 입력으로 주어지는 K보다 항상 크다의 반례로 While문 탈출\n",
        "            break #탈출\n",
        "        \n",
        "        sum1 +=first\n",
        "        M -= 1 # 더해지는 횟수 차감\n",
        "        \n",
        "    if M == 0:\n",
        "        break\n",
        "        \n",
        "    sum1 += second\n",
        "    M -=1\n",
        "\n",
        "print(sum1)\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(3):\n",
        "    print(1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6lztc7_vjC2j",
        "outputId": "406caf1c-4bc4-4256-aee6-59c99a2ce8d9"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "1\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#큰 수의 법칙 version2\n",
        "#이중 for문이라 시간은 오래 걸릴 수도 있다.\n",
        "N,M,K = map(int, input().split()) #배열 숫자 갯수, 총 더하는 횟수, K는 인덱스가 같은 것을 연속성 사용 시 최대 횟수\n",
        "\n",
        "data = list(map(int, input().split()))\n",
        "\n",
        "data.sort(reverse=True)\n",
        "\n",
        "#인덱싱으로 설정하는 이유는, 같은 수여도 인덱싱이 다르면 다른 숫자 취급\n",
        "#최대, 두번째 큰 수라고 보긴 어려울 수도 있다\n",
        "#max함수를 사용하면 안되는 이유\n",
        "\n",
        "f1 = data[0] \n",
        "f2 = data[1]\n",
        "\n",
        "result = [] # 빈 리스트 후 \n",
        "\n",
        "for j in range(int(M % K)):\n",
        "    for i in range(K):\n",
        "        result.append(f1)\n",
        "    result.append(f2)\n",
        "\n",
        "print(sum(result))\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0WnDEgtOoT8X",
        "outputId": "c64a7343-4602-4b7f-fc38-ee1160c7b9e3"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 8 3\n",
            "2 4 5 4 6\n",
            "46\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "8 % 3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jJgGlcontR-o",
        "outputId": "ebe14d29-585c-4875-823e-4578eb533e2b"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "5ZsH095IuOe0"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}