{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "quick_sort",
      "provenance": [],
      "authorship_tag": "ABX9TyM+z+EAAr+Nl46de4zg4HYB"
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
      "source": [
        "def quick_sort(arr): #퀵 정렬\n",
        "    __sort(arr, 0 , len(arr) -1) #__sort에 배열, 인덱스 0, 전체길이 -1 이 들어있다\n",
        "\n",
        "def __sort(arr, low, high): #__sort함수 정의\n",
        "    if low >= high: #low가 high보다 크다면\n",
        "        return #그냥 지나가라\n",
        "    \n",
        "    pivot = (low + high) // 2 #pivot은 양 끝 점의 합/2 지점\n",
        "    pivot_val = arr[pivot] #pivo값은 배열의 부분(중간지점)\n",
        "\n",
        "    left, right = low, high #left = low, right = high할당\n",
        "    while left <= right: # left가 더 클 떄까지 진행\n",
        "        while arr[left] < pivot_val: #왼쪽값이 피봇보다 커질 때까지 진행\n",
        "            left += 1 #작은 상황이면 왼쪽으로 숫자 1개 생김\n",
        "        \n",
        "        while arr[right] > pivot_val: #위의 상황이라면\n",
        "            right -=1 #오른쪽은 하나 줄어들죠\n",
        "\n",
        "        if left <= right:\n",
        "            arr[right], arr[left] = arr[left], arr[right]\n",
        "            left += 1\n",
        "            right -=1\n",
        "\n",
        "    __sort(arr, low, right) #__sort함수 적용\n",
        "    __sort(arr, left, high) #--sort함수 적용"
      ],
      "metadata": {
        "id": "bKKaErAxOVxE"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ ==\"__main__\": #main.py\n",
        "    arr = [9,1,6,3,7,2,8,4,5,0] #배열\n",
        "    quick_sort(arr) #퀵 정렬\n",
        "    print(arr) #결과값\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1xMz-a29LmM3",
        "outputId": "6a116cd9-cde5-427e-a505-8857c717e25d"
      },
      "execution_count": 3,
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
        "id": "5NZxGbAiQbtK"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}