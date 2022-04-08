{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "merge_sort",
      "provenance": [],
      "authorship_tag": "ABX9TyN+4Bb6NxBXlGLhOBW5O4kd"
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
        "id": "08-_hWBVrC9k"
      },
      "outputs": [],
      "source": [
        "def merge_sort(arr): #merge정렬\n",
        "    if len(arr) <= 1: # 길이가 1보다 작다면 \n",
        "        return #그냥 return\n",
        " \n",
        "    #나누기\n",
        "    mid = len(arr)//2 #중간 부분\n",
        "    left = arr[:mid]#분할된 인쪽 리스트\n",
        "    right = arr[mid:] #분할된 오른쪽 리스트\n",
        "\n",
        "    merge_sort(left) #왼쪽 리스트에 적용\n",
        "    merge_sort(right) #오른쪽 리스트에 적용\n",
        "\n",
        "    #정복\n",
        "\n",
        "    i = 0 #left idx\n",
        "    j = 0 #right idx\n",
        "    k = 0 # arr idx\n",
        "\n",
        "    while i < len(left) and j < len(right): #i와 j가 커지기 전까지 계속 실행\n",
        "        if left[i] <= right[j]: # 오른쪽이 더 많다면\n",
        "            arr[k] = left[i] #인덱스 부분과 왼쪽이 같다\n",
        "            i +=1 #1증가\n",
        "        else:\n",
        "            arr[k] = right[j] #인덱스 부분과 오른쪽이 같다면\n",
        "            j += 1#1증가\n",
        "        k +=1 #인덱스 1 증가\n",
        "    \n",
        "#전체 정렬이 되고 왼쪽 오른쪽 부분만 남은 상태\n",
        "\n",
        "    while i < len(left): # 왼쪽보다 클 뗴끼지하기\n",
        "        arr[k] = left[i] # 같다\n",
        "        i += 1 #왼쪽 리스트 1 증가\n",
        "        k += 1 #인덱스 증가\n",
        "\n",
        "    while j < len(right): # 오른쪽 클때까지\n",
        "        arr[k] = right[j] #같다\n",
        "        j += 1 #오른쪽 인덱스 증가\n",
        "        k += 1  # 인덱스 증가\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == \"__main__\": #main.py\n",
        "    arr = [9,1,6,3,7,2,8,4,5,0] #배열\n",
        "    merge_sort(arr) #병합정렬 적용\n",
        "    print(arr) #결과값"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "epWbymT1tGJE",
        "outputId": "0e9b8f10-1720-4dcb-ce09-dd5a10b2b10d"
      },
      "execution_count": 5,
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
        "id": "XLTnLyPwtp7i"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}