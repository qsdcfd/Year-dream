{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "151~160",
      "provenance": [],
      "authorship_tag": "ABX9TyOuzj9rARj2EE34MQ5rXtVc"
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
        "id": "zi9RUHSTEAaM",
        "outputId": "9d903bd9-ca45-4fd6-f77f-1bd1f645d75e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-20\n",
            "-3\n",
            "-20\n",
            "-3\n"
          ]
        }
      ],
      "source": [
        "#151 : 리스트에는 네 개의 정수가 저장되어있다. for문을 사용해서 리스트의 음수 출력\n",
        "\n",
        "리스트 = [3, -20, -3, 44]\n",
        "\n",
        "for negative1 in 리스트[1:3]:\n",
        "    print(negative1)\n",
        "\n",
        "for negative1 in 리스트:\n",
        "    if negative1 < 0:\n",
        "        print(negative1)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#152 for문을 사용해서 3의 배수만 출력\n",
        "\n",
        "리스트 = [3,100,23,44]\n",
        "\n",
        "for three in 리스트:\n",
        "    if three % 3 ==0:\n",
        "        print(three)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wwSBydkhE2e_",
        "outputId": "1077ca3d-c660-45a0-86ae-a1ca4c33c37e"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#153: 리스트에서 20보다 작은 3의 배수 출력\n",
        "\n",
        "리스트 = [13,21,12,14,30,18]\n",
        "\n",
        "for threes in 리스트:\n",
        "    if threes % 3 == 0 and threes <20:\n",
        "        print(threes)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BhdkVcm7FRQt",
        "outputId": "7129b598-dbfc-4433-a5a6-b0a4ca687a65"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "12\n",
            "18\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#154: 리스트에서 세 글자 이상의 문자를 화면에 출력하라\n",
        "\n",
        "리스트 = [\"I\", \"study\", \"python\", \"language\", \"!\"]\n",
        "\n",
        "for text1 in 리스트:\n",
        "    if len(text1) >=3:\n",
        "        print(text1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mY4LXOPMFfwn",
        "outputId": "0e9881d4-e790-4959-df8d-d0217b2f8146"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "study\n",
            "python\n",
            "language\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#155: 리스트에서 대문자만 화면에 출력하라\n",
        "\n",
        "리스트 = [\"A\", \"b\", \"c\", \"D\"]\n",
        "\n",
        "for big in 리스트:\n",
        "    if big.isupper() == True:\n",
        "        print(big)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WK9aX2ntFtde",
        "outputId": "74de7f1e-0c6b-4285-8781-713398b5a74e"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A\n",
            "D\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#156: 리스트에서 소문자만 화면에 출력\n",
        "리스트 = [\"A\", \"b\", \"c\", \"D\"]\n",
        "\n",
        "for small in 리스트:\n",
        "    if small.islower() == True:\n",
        "        print(small)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "twD595_ZGCqG",
        "outputId": "58714521-fa0d-4ff7-caaf-bf8b35e34919"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "b\n",
            "c\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#157: 이름의 첫 글자를 대문자로 변경해서 출력\n",
        "\n",
        "리스트 = ['dog', 'cat', 'parrot']\n",
        "\n",
        "for bigs in 리스트:\n",
        "    print(bigs[0].upper() + bigs[1:])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5jWQE1K4GKmr",
        "outputId": "2723779c-ed86-47af-deb1-5a73073b639a"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dog\n",
            "Cat\n",
            "Parrot\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#158: 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력\n",
        "\n",
        "리스트 = ['hello.py', 'ex01.py', 'intro.hwp']\n",
        "\n",
        "for file1 in 리스트:\n",
        "    file2 = file1.split(\".\")\n",
        "    print(file2[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WTPEqAzOGZek",
        "outputId": "e3619ffe-6873-4758-efd8-e350e1b44da1"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello\n",
            "ex01\n",
            "intro\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#159: 파일 이름이 저장된 리스트에서 확장자가 .h\n",
        "리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']\n",
        "\n",
        "\n",
        "리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']\n",
        "\n",
        "for file3 in 리스트:\n",
        "    file4 = file3.split('.')\n",
        "\n",
        "    if file4[1] == 'h':\n",
        "        print(file3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r4smlXhHI1IK",
        "outputId": "6f125143-6b4c-4278-a7b8-98ec138c8b90"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "intra.h\n",
            "define.h\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#160: 파일 이름이 저장된 리스트에서 확장자가 .h or .c인 파일 이름 출력\n",
        "\n",
        "리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']\n",
        "\n",
        "for file3 in 리스트:\n",
        "    file4 = file3.split('.')\n",
        "\n",
        "    if file4[1] == 'h'or file4[1] == 'c':\n",
        "        print(file3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CvTVX0HSGvYt",
        "outputId": "eea5ffd7-6278-497c-bfdf-046144a68a10"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "intra.h\n",
            "intra.c\n",
            "define.h\n"
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
        "id": "-b9PotAYIrHk"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}