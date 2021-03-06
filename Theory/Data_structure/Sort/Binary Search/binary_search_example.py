{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "binary_search_example의 사본",
      "provenance": [],
      "authorship_tag": "ABX9TyM9i6HE+mdi0ASHqr5oy1eM"
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
        "id": "qZDCwQvSlRp5"
      },
      "outputs": [],
      "source": [
        "def binary_search(arr, target): #이진탐색 함수, target는 찾아야하느 값\n",
        "    l = 0 #처음엔 0으로 초기화 l은 list의 약자입니다.\n",
        "    r = len(arr) - 1 #배열의 총 길이에서 하나를 뺀 값이 r (짝수화)\n",
        "\n",
        "    while l <= r: #l > r이되면 while문 종료로 그 전까지 계속 진행\n",
        "        m = (l + r) // 2 #이진탐색이 절반의 위치를 구하는 방식이므로 그 방식을 수식화\n",
        "        if arr[m] < target: # 타겟이 arr[m]보다 크다면\n",
        "            l = m +1 #한 칸 더 옆에서 실행\n",
        "        elif arr[m] > target: #작다면\n",
        "            r = m -1 #한 칸 뒤에서 실행\n",
        "        else:\n",
        "            return m #둘 다 아니면 그냥 m출력\n",
        "    return -1 #while문이 끝나면 -1출력\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == \"__main__\": #main.py\n",
        "    arr = [1,2,3,4,5,6,7,8,9] #배열의 총 길이\n",
        "    print(binary_search(arr,3)) #타켓이 배열보다 작으므로 3-1 =2\n",
        "    print(binary_search(arr,7)) #타켓이 배열보다 작으므로 7-1 =6\n",
        "    print(binary_search(arr,15)) #l > r이므로 -1 출력"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OGS6__H6nYF4",
        "outputId": "d515485f-2cc9-4df3-dc17-70e97292b966"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "6\n",
            "-1\n"
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
        "id": "LWQG6ZNLn2SW"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}