{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "bubble_sort",
      "provenance": [],
      "authorship_tag": "ABX9TyMCp4s0NSa/Y+VU8IGeuXTm"
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
        "id": "2MHnz2at9h2L"
      },
      "outputs": [],
      "source": [
        "def bubble_sort(arr): #버블 정렬 함수 구현\n",
        "#for문의 의미는 인접한 요소들의 위츨ㄹ 말하는 것입니다.\n",
        "\n",
        "    for i in range(len(arr) -1 ): # 배열 길이보다 하나 작은 값을 천천히 넣기\n",
        "        for j in range(len(arr) - i -1): # j에는 배열 길이 - i - 1 \n",
        "            if arr[j] > arr[j+1]: #만약 j의 위치 값이  j+1의 위치 값보다 크다면\n",
        "                arr[j], arr[j+1] = arr[j+1], arr[j] # 자리를 교환해라"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == \"__main__\": #main.py\n",
        "    arr = [9,1,6,3,7,2,8,4,5,0] #정렬해야하는 값\n",
        "    bubble_sort(arr) #버블함수 적용\n",
        "\n",
        "    print(arr) # 결과값"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VVbny3pwcUrG",
        "outputId": "f6e541cd-f840-44ce-a108-0e669f65dd45"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
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
        "id": "U5hOnPgLceqH"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}