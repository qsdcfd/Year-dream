{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "insertion sort",
      "provenance": [],
      "authorship_tag": "ABX9TyNxXq7su4otssEnw/xB1Vi1"
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
      "execution_count": 3,
      "metadata": {
        "id": "tNp_hgppgSoj"
      },
      "outputs": [],
      "source": [
        "def insertion_sort(arr): #삽입 정렬\n",
        "    for i in range(1, len(arr)): #인덱스 1부터 시작하는 것을 의미\n",
        "        key = arr[i] #key는 곧 해당 i번째 인덱스 위치의 값\n",
        "        j = i -1 #인접한 것을 비교하기에 그 전 위치의 값과 비교\n",
        "        while j >= 0 and arr[j] > key: #j <0 그리고 arr[j] <=key될 때까지 하기\n",
        "            arr[j + 1] = arr[j] #인덱스의 위치가  i와 j가 같을 때\n",
        "            j -= 1 #한 위치 옮겨야한다\n",
        "        arr[j + 1] = key # j+1의 값은 곧 key"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == \"__main__\": #main.py\n",
        "    arr = [9,1,6,3,7,2,8,4,5,0] # 배열값\n",
        "    insertion_sort(arr) #삽입 정렬 함수 구현\n",
        "    print(arr) # 결과값"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ckNive_fg-aC",
        "outputId": "e665d5c0-460d-4899-b207-fd1ac9806005"
      },
      "execution_count": 4,
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
        "id": "hjAcntZ2hMis"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}