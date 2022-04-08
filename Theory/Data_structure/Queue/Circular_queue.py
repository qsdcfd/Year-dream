{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Circular_queue",
      "provenance": [],
      "authorship_tag": "ABX9TyN9LvfmEjgm5AbMtJ6b7zyO"
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
        "id": "E0ZgKNqM29bT"
      },
      "outputs": [],
      "source": [
        "class CircularQueue: #원형 큐 구현\n",
        "    def __init__(self, max_size): #첫 시작은 국룰로 __init__!!, 최대 사이즈를 인자\n",
        "        self.elements = [None] * (max_size + 1) #인자는 최대 사이즈보다 한 칸 더 갈 수 있디\n",
        "        self.front = 0 # front부분 0으로 초기화\n",
        "        self.rear = 0 # rear부분을 0으로 초기화\n",
        "        self.max_size = max_size + 1 #최대 사이즈의 +1 한 것이 최대 사이즈\n",
        "\n",
        "    def is_full(self): #다 채워져있을 때\n",
        "        return (self.rear + 1) % self.max_size == self.front #rear의 한 칸 더 간 게 front와 맞다면 full!!\n",
        "\n",
        "    def is_empty(self): #비어있을 때\n",
        "        return self.front == self.rear #front와 rear가 한 공간일 때\n",
        "\n",
        "    def clear(self): # 비우는 함수(초기화)\n",
        "        self.front = 0 #front를 0으로 초기화\n",
        "        self.rear = 0 #rear을 0으로 초기화\n",
        "\n",
        "    def offer(self, data): #삽입 함수로 data가 인자이다\n",
        "        if self.is_full(): #만약 full 이라면\n",
        "            raise RuntimeError(\"Queue is full\") #큐가 다 채워졌다라고 말하기\n",
        "\n",
        "        self.rear = (self.rear + 1) % self.max_size #rear + 1 =front상태고 다 꽉 찬 상태입니다.\n",
        "        self.elements[self.rear] = data #rear에 데이터가 있을 겁니다.\n",
        "\n",
        "    def poll(self): #데이터를 추출하는 함수\n",
        "        if self.is_empty(): #비어있다면\n",
        "            raise RuntimeError(\"Queue is empty\") #큐는 비어있다고 호출\n",
        "        self.front = (self.front + 1) % self.max_size #front가 곧 최대크기\n",
        "        return self.elements[self.front] # front = 0\n",
        "\n",
        "    def size(self): #길이\n",
        "        if self.front <= self.rear: #rear 부분이 인덱스가 더 크다면\n",
        "            return self.rear - self.front #rear- front로 추출\n",
        "        return self.max_size - self.front + self.rear #front가 더 길다면 최대 길이 - -front + rear\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == \"__main__\": #main.py함수이다\n",
        "    q = CircularQueue(5) #매번 CicrularQueue를 사용할 수 없기에 q를 이용하여 할당하고 size =5\n",
        "    for e in range(5): #0~4까지의 숫자 넣기\n",
        "        print(f\"is_full: {q.is_full()}, is_empty:{q.is_empty()}, size: {q.size()}\") #꽉 찼는지 확인, 비었는지 확인, 사이즈 확인\n",
        "        q.offer(e) #숫자 삽입\n",
        "        print(f\"q.offer({e})\") # 잘 들어갔나 확인\n",
        "        print(f\"is_full: {q.is_full()}, is_empty: {q.is_empty()}, size:{q.size()}\") #다시 한번 꽉 찼는지 확인, 비었는지 확인, 사이즈 확인\n",
        "\n",
        "    print(\"-------------------------------\") # 줄 방지\n",
        "    while q.size() > 0: #size가 0보다 크다면\n",
        "        print(f\"is_full: {q.is_full()}, is_empty: {q.is_empty()}, size: {q.size()}\")#다시 한번 꽉 찼는지 확인, 비었는지 확인, 사이즈 확인\n",
        "        print(f\"q.poll(): {q.poll()}\")#숫자 뻬기"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KhTsel3Z7dIY",
        "outputId": "4ebee53e-5c92-43fb-d4ce-9ae6cab7ca9e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "is_full: False, is_empty:True, size: 0\n",
            "q.offer(0)\n",
            "is_full: False, is_empty: False, size:1\n",
            "is_full: False, is_empty:False, size: 1\n",
            "q.offer(1)\n",
            "is_full: False, is_empty: False, size:2\n",
            "is_full: False, is_empty:False, size: 2\n",
            "q.offer(2)\n",
            "is_full: False, is_empty: False, size:3\n",
            "is_full: False, is_empty:False, size: 3\n",
            "q.offer(3)\n",
            "is_full: False, is_empty: False, size:4\n",
            "is_full: False, is_empty:False, size: 4\n",
            "q.offer(4)\n",
            "is_full: True, is_empty: False, size:5\n",
            "-------------------------------\n",
            "is_full: True, is_empty: False, size: 5\n",
            "q.poll(): 0\n",
            "is_full: False, is_empty: False, size: 4\n",
            "q.poll(): 1\n",
            "is_full: False, is_empty: False, size: 3\n",
            "q.poll(): 2\n",
            "is_full: False, is_empty: False, size: 2\n",
            "q.poll(): 3\n",
            "is_full: False, is_empty: False, size: 1\n",
            "q.poll(): 4\n"
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
        "id": "gOiOlzer8WpB"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}