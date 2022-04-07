{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "stack_example",
      "provenance": [],
      "authorship_tag": "ABX9TyNIlzqmlnJIZw5qrL1hqwHQ"
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
        "id": "l8RUpRL8m7O7"
      },
      "outputs": [],
      "source": [
        "#Stack를 직접 클래스와 함수로 만들어서 구현하기\n",
        "\n",
        "class Stack:\n",
        "    def __init__(self): #클래스의 첫 함수는 __init__로 하는 게 국룰\n",
        "        self.head = Node() #head에 빈 노드가 있는 상태 (Null)\n",
        "        self._size = 0 #size 0으로 초기화\n",
        "\n",
        "    def push(self, data): #data를 넣는 푸쉬\n",
        "        new_node = Node() #처음에 node는 없는 상태\n",
        "        new_node.data = data # data 할당\n",
        "        new_node.next = self.head.next #head의 다음에 새로운 노드가 들어간다\n",
        "        self.head.next = new_node #head의 다음은 새로운 노드 (들어온 상태)\n",
        "        self._size += 1 #들어왔으니 사이즈가 증가\n",
        "\n",
        "    def pop(self): #data를 빼는 pop\n",
        "        if self.size == 0: #size가 0, 즉 노드가 없다면\n",
        "            return None #빈 노드라고 출력\n",
        "\n",
        "        ret = self.head.next #ret눈 해드 다음에 오는 것\n",
        "        self.head.next = ret.next # 헤드 다음이 ret의 다음\n",
        "        self._size -= 1 # 데이터를 뺐으니 사이즈 감소\n",
        "        return ret.data # 뺀 후 그 데이터 추출\n",
        "\n",
        "    def peek(self): #peek기능 확인\n",
        "        if self._size == 0: #size가 0이라면 추출할 데이터가 없으니 None출력\n",
        "            return None #None 출력\n",
        "        return self.head.next.data #그게 아니라면 가장 최근에 들어온 거 출력\n",
        "\n",
        "    def size(self):# size함수\n",
        "        return self._size # 몇 개의 숫자가 들어있나 체크\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node:\n",
        "    def __init__(self):\n",
        "        self.next = None\n",
        "        self.data = None"
      ],
      "metadata": {
        "id": "eJj4DYbnn2vJ"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == \"__main__\":\n",
        "    s = Stack()\n",
        "    print(\"s.push(3)\") #3넣자고 출력\n",
        "    s.push(3)#3넣기\n",
        "    print(\"s.push(5)\")#5넣자고 출력\n",
        "    s.push(5)#5넣기\n",
        "    print(\"s.push(1)\") # 1넣자고 출력\n",
        "    s.push(1) #1넣기\n",
        "    print(\"s.push(9)\")# 9넣자고 출력\n",
        "    s.push(9)#9 넣기\n",
        "    print(f\"s.size(): {s.size()}\") #몇 개의 숫자가 들어왔는지 출력\n",
        "    print(f\"s.peek(): {s.peek()}\")# 마지막에 들어온 숫자\n",
        "    print(f\"s.pop(): {s.pop()}\")# 마지막에 있는 것부터 뺀다\n",
        "    print(f\"s.pop(): {s.pop()}\")#그 다음\n",
        "    print(f\"s.pop(): {s.pop()}\")#그 다다음\n",
        "    print(f\"s.pop(): {s.pop()}\")#그 다다다음\n",
        "    s.peek()#다 빠졌나 확인\n",
        "    print(f\"s.peek(): {s.peek()}\") #다 뺀 상태라서 데이터가 없어서 none 출력\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8lqaDPWon8H4",
        "outputId": "9442c532-bc53-49ba-be8a-2b6edfec2455"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "s.push(3)\n",
            "s.push(5)\n",
            "s.push(1)\n",
            "s.push(9)\n",
            "s.size(): 4\n",
            "s.peek(): 9\n",
            "s.pop(): 9\n",
            "s.pop(): 1\n",
            "s.pop(): 5\n",
            "s.pop(): 3\n",
            "s.peek(): None\n"
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
        "id": "QhwFv8wKosql"
      },
      "execution_count": 4,
      "outputs": []
    }
  ]
}