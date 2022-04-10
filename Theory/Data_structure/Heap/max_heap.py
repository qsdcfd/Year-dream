{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "max_heap",
      "provenance": [],
      "authorship_tag": "ABX9TyMjPJbyAJwqQeSwuGHGlp2/"
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
        "class MaxHeap: #최대 힙\n",
        "    def __init__(self): #시작은 국룰\n",
        "        self.data = [] #빈 리스트 만들어서 숫자 넣기\n",
        "    \n",
        "    def size(self): #사이즈 함수\n",
        "        return len(self.data) #길이 반환\n",
        "\n",
        "    def insert(self, value): #삽입함수\n",
        "        self.data.append(value) #빈 리스트인 data에 값 넣기\n",
        "        self.heapify(len(self.data) -1) #전체 - 1\n",
        "\n",
        "    def pop(self): #빼는 함수\n",
        "        ret = self.data[0] #data의 첫 부분\n",
        "        self.data[0] = self.data[-1] #같다\n",
        "        self.data.pop() #데이터빼기\n",
        "        self.max_heapify() #최대힙 구하기\n",
        "        return ret #변화된 값 확인\n",
        "\n",
        "    def peek(self): # 읽기만하는 함수\n",
        "        return  self.data[0] #확인작업\n",
        "\n",
        "    def max_heapify(self, index): #최대 힙\n",
        "        left = 2 * index + 1 #왼쪽부분 2개 건너뛰고 한 칸 더\n",
        "        right = 2 * index + 2 #오른쪽부분 2개 건너뛰고 두 칸 더\n",
        "        largest = index #최대\n",
        "\n",
        "        if left < len(self.data) and self.data[left] > self.data[largest]:\n",
        "            largest = left\n",
        "        if right < len(self.data) and self.data[right] > self.data[largest]:\n",
        "            largest = right\n",
        "        if largest != index:\n",
        "            self.data[index], self.data[largest] = self.data[largest], self.data[index]\n",
        "            self.max_heapify(largest)\n",
        "\n",
        "    def heapify(self, index):\n",
        "        parent = (index - 1) // 2\n",
        "        if parent >= 0:\n",
        "            if self.data[index] > self.data[parent]:\n",
        "                self.data[index], self.data[parent] = (\n",
        "                    self.data[parent],\n",
        "                    self.data[index],\n",
        "                )\n",
        "                self.heapify(parent)\n",
        "    "
      ],
      "metadata": {
        "id": "c3Adj0cdO-g5"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MzE5gQ6Xy67W",
        "outputId": "bd8d6cba-cb04-4a91-b5c0-72a58f9cd9e8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "max_heap.insert(0)\n",
            "max_heap.peek(): 0\n",
            "max_heap.insert(1)\n",
            "max_heap.peek(): 1\n",
            "max_heap.insert(2)\n",
            "max_heap.peek(): 2\n",
            "max_heap.insert(3)\n",
            "max_heap.peek(): 3\n",
            "max_heap.insert(4)\n",
            "max_heap.peek(): 4\n",
            "===========================================\n",
            "max_heap.size(): 5\n",
            "max_heap.pop(): 4\n",
            "max_heap.size(): 4\n",
            "max_heap.pop(): 3\n",
            "max_heap.size(): 3\n",
            "max_heap.pop(): 2\n",
            "max_heap.size(): 2\n",
            "max_heap.pop(): 1\n",
            "max_heap.size(): 1\n",
            "max_heap.pop(): 0\n"
          ]
        }
      ],
      "source": [
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    max_heap = MaxHeap()\n",
        "    for i in range(5):\n",
        "        print(f\"max_heap.insert({i})\")\n",
        "        max_heap.insert(i)\n",
        "        print(f\"max_heap.peek(): {max_heap.peek()}\")\n",
        "\n",
        "    print(\"===========================================\")\n",
        "    for _ in range(5):\n",
        "        print(f\"max_heap.size(): {max_heap.size()}\")\n",
        "        print(f\"max_heap.pop(): {max_heap.pop()}\")"
      ]
    }
  ]
}