{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "linked_queue_example",
      "provenance": [],
      "authorship_tag": "ABX9TyP/Qz7uzJZ1WFfKmGPFIbNi"
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
        "id": "ZeJE2juCsLfo"
      },
      "outputs": [],
      "source": [
        "##class Node를 짜는 것입니다.\n",
        "\n",
        "class Node:\n",
        "    def __init__(self, data, next_=None): #data를 할당하고 그 다음에 올 인자를 초기화\n",
        "        self.data = data # 할당\n",
        "        self.next = next_ #초기화\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#연결형 큐 클래스를 작성해보겠습니다.\n",
        "\n",
        "class LinkedQueue:\n",
        "\n",
        "    def __init__(self): #첫 함수는 항상 국룰\n",
        "        self._size = 0 # 길이는 0으로 초기화\n",
        "        self.head = Node(None) # head에 처음엔 아무 것도 없는 더미\n",
        "        self.tail = self.head # tail도 head와 마찬가지\n",
        "\n",
        "    def offer(self, data): #offer함수는 push함수와 동일한 데이터 넣는 것입니다.\n",
        "        node = Node(data) #node에 data 넣기\n",
        "        self.tail.next = node# tail다음에 Node \n",
        "        self.tail = self.tail.next # tail 다음에 node 담김\n",
        "        self._size += 1 #길이 1 증가\n",
        "\n",
        "    def poll(self): # 데이터 빼기\n",
        "        if self._size == 0: # 길이가 0이라면\n",
        "            raise RuntimeError(\"Empty\") # 비어있다는 문구 출력\n",
        "\n",
        "        ret = self.head.next #head를 넘어 다음 노드\n",
        "        self.head.next = ret.next # head의 다음 노드는 ret할당\n",
        "        ret.next = None # ret는 비어있다[데이터가 잘 빠짐]\n",
        "        self._size -= 1# 데이터의 길이가 하나 줄어든다\n",
        "        if self.head.next is None: # head다음에 노드가 없다면\n",
        "            self.tail = self.head # tail이랑 head가 같은 관계\n",
        "        return ret.data # 그냥 data출력\n",
        "\n",
        "    def peek(self): #처음에 빠지는 데이터 추출\n",
        "        if self._size == 0: # 아무것도 없다면\n",
        "            raise RuntimeError(\"Empty\") #비어있다는 말을 출력\n",
        "        return self.head.next.data # head다음에 데이터를 반환\n",
        "\n",
        "    def size(self): #길이 알려주는 함수\n",
        "        return self._size # 길이 반환\n",
        "\n",
        "    def clear(self):# 초기화\n",
        "        self.head.next = None # head 다음 노드 없다\n",
        "        self.tail = self.head # head 와 tail이 같다\n",
        "        self._size = 0 # 사이즈는 0\n",
        " \n"
      ],
      "metadata": {
        "id": "7vwXa6x8wPmc"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ =='__main__': #main.py\n",
        "    q = LinkedQueue() # LinkedQueue()를 계속 쓸 수 없으니 q로 할당\n",
        "    for elem in [5,3,6,8,9,10]: #[5,3,6,8,9,10]하나씩 빠진다\n",
        "        print(f\"q.offer({elem})\") #offer함수 적용\n",
        "        q.offer(elem)#데이터 넣기\n",
        "\n",
        "    print(f\"q.size(): {q.size()}\") #길이 확인[ 데이터 삽입이 잘 되었나?]\n",
        "    while q.size() > 0: #q,size가 0보다 크다면\n",
        "        print(f\"q.peek(): {q.peek()}\") #peek를 구해서 처음에 빠지는 숫자 확인\n",
        "        print(f\"q.pop(): {q.poll()}\") #데이터 빼기\n",
        "\n",
        "    print(f\"q.size(): {q.size()}\") #길이 확인을 통해서 데이터가 잘 빠졌나 확인"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TkLayhDnxYLX",
        "outputId": "5ad351ab-1f83-448d-9692-fa906e125485"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "q.offer(5)\n",
            "q.offer(3)\n",
            "q.offer(6)\n",
            "q.offer(8)\n",
            "q.offer(9)\n",
            "q.offer(10)\n",
            "q.size(): 6\n",
            "q.peek(): 5\n",
            "q.pop(): 5\n",
            "q.peek(): 3\n",
            "q.pop(): 3\n",
            "q.peek(): 6\n",
            "q.pop(): 6\n",
            "q.peek(): 8\n",
            "q.pop(): 8\n",
            "q.peek(): 9\n",
            "q.pop(): 9\n",
            "q.peek(): 10\n",
            "q.pop(): 10\n",
            "q.size(): 0\n"
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
        "id": "UDI70grJyH00"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}