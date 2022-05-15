{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "프로그래머스 가장 큰 수",
      "provenance": [],
      "authorship_tag": "ABX9TyNS2Lo9+qB7XoKjvsIMZOpt"
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
      "execution_count": null,
      "metadata": {
        "id": "h_kj7jP3PjN8"
      },
      "outputs": [],
      "source": [
        "def solution(numbers):\n",
        "    \"\"\"\n",
        "    숫자를 리스트로 받고난 후에 그 숫자끼리 조합을 합니다.\n",
        "    그리고 나서 가장 큰 수를 int로 바꾸면 됩니다\n",
        "    \"\"\"\n",
        "    numbers = list(map(str,numbers)) #숫자입력\n",
        "    numbers.sort(key=lambda x:x*3, reverse=True) #숫자를 정렬하는데 이때 받은 같은 수를 3번 반복한 후 인덱싱으로 뽑아내면([0]) 앞자리 큰 수로 정렬됩니다.\n",
        "    return str(int(''.join(numbers))) #공백으로 숫자를 합쳐서 정수로 바꿈"
      ]
    }
  ]
}