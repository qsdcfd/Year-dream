{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "stack.example",
      "provenance": [],
      "authorship_tag": "ABX9TyMpEKiUF13NIdH4gtMfUqbc"
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
        "id": "aCD3_HPKrNZW"
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
        "        return self._size # 몇 개의 숫자가 들어있나 체크"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class Node: #노드 클래스 구현\n",
        "    def __init__(self): #클래스의 첫 시작\n",
        "        self.next = None # 처음이니까 당연히 초기화\n",
        "        self.data = None #데이터도 초기화"
      ],
      "metadata": {
        "id": "ZgogAWVtrgEi"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == \"__main__\": # main.py파일\n",
        "    s = Stack() #Stack()을 매번 쓰는 건 비효율이기에 할당\n",
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
        "    print(f\"s.peek(): {s.peek()}\") #다 뺀 상태라서 데이터가 없어서 none 출력"
      ],
      "metadata": {
        "id": "oM9LxJKNro7M"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}