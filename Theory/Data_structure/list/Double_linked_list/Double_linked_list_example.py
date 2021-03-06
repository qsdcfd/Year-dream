{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Double_linked_list_example",
      "provenance": [],
      "authorship_tag": "ABX9TyPGTqGHiaV1F4LWcP+qF8L9"
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
        "id": "semwYJzP1ZBi"
      },
      "outputs": [],
      "source": [
        "#Node를 클래스 작성하면 편리합니다.\n",
        "#왜냐하면, 초기화나 할당을 계속 안해도 됩니다. 이것이 상속과 클래스의 장점이죠\n",
        "#이번 실습에서 중요한 것은 양방향 연결 리스트에서 previous와 next가 어떻게 연결이 되는가 입니다.\n",
        "#모든 값의 시작은 초기화입니다. 그래야 저희가 원하는 값을 넣기 편하거든요\n",
        "\n",
        "class Node: #파이썬답게 class 이름을 명시적으로 node로 지정\n",
        "    def __init__(self, data, prev_=None, next_=None): #prev_ and next_를 초기화를 시킵니다.\n",
        "        self.data = data #할당\n",
        "        self.prev = prev_ # 할당\n",
        "        self.next = next_ #힐딩\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#클래스로 DoubleLinkedList 구현 코드 짜기\n",
        "\n",
        "class DoubleLinkedList:\n",
        "    def __init__(self):\n",
        "        self.head = Node(None) #head는 더미노드이기에 초기화를 시킵니다. *더미노드: Node가 없는 것\n",
        "        self.tail = Node(None) #tail는 더미노드이기에 초기화를 시킵니다.\n",
        "        self._size = 0# size도 시작이면 0이겠죠?\n",
        "\n",
        "        self.head.next = self.tail #head의 next는 tail입니다. 연결리스트 구조를 보시면 헤드 - 테일이 기본 구조입니다. 여기서 점점 길어지긴 하지만요\n",
        "        self.tail.prev = self.head #tail의 previous는 head입니다. \n",
        "\n",
        "    def size(self): #size(길이)에 관련한 함수입니다.\n",
        "        return self._size # 0을 반환합니다.\n",
        "\n",
        "    def add(self, data): # Node가 추가되는 함수\n",
        "        last = self.tail.prev # last는 head\n",
        "        new_node = Node(data, last, self.tail) #새롭게 들어올 노드가 들어올 수 있도록 초기화\n",
        "        last.next = new_node# head 다음에 node가 추가됩니다\n",
        "        self.tail.prev = new_node # 구조의 변화: 헤드 - new_node - 테일로 바뀌었습니다. node가 추가되었기 때문이지요\n",
        "        self._size += 1 # 새로운 node가 들어오고 구조의 길이도 늘었으니 사이즈를 증가해야겠죠?! 그것을 의미합니다.\n",
        "\n",
        "\n",
        "    def insert(self, index, data): # 원하는 인덱스 위치에 값을 넣는 insert 구현 함수\n",
        "        if index > self._size or index < 0: #index의 위치가 사이즈보다 크거나 0보다 작을 경우\n",
        "            raise RuntimeError(\"Index out of error\") # 인덱스가 범위를 넘었다는 에러 호출\n",
        "\n",
        "        prev, current = None, None #초기화\n",
        "        i = 0 # 초기화\n",
        "        if index < self._size // 2: #index가 전체 사이즈의 절반보다 작다면(절반으로 지정한 이유는 양방향으로 숫자 삽입이 가능하기 때문이다)\n",
        "            prev = self.head # 더미노드(head)\n",
        "            current = self.head.next # tail부터 숫자 넣기\n",
        "            while i < index: # i가 index보다 클 때까지 돌린다\n",
        "                prev = prev.next # prev다음으로 이동\n",
        "                current = current.next # current다음으로 이동\n",
        "                i +=1 #1 증가\n",
        "        else: #index >= self._size //2\n",
        "            current = self.tail # current의 노드엔 아무것도 없다\n",
        "            prev = self.tail.prev # prev의 노드엔 아무것도 없다\n",
        "            while i < (self._size - index): #i가 >= (self._size - index)가 될 때까지 돌려짐\n",
        "                current = current.prev #current는 이전 걸로 이동\n",
        "                prev = prev.prev #이전의 이전걸로 이동\n",
        "                i += 1 #1 증가\n",
        "\n",
        "        new_node = Node(data,prev, current) # 새로운 노드가 class None 할당\n",
        "        current.prev = new_node # current에 새로운 노드 할당\n",
        "        prev.next = new_node # previous에 새로운 노드 할당\n",
        "        self._size += 1 # size 증가\n",
        "\n",
        "    def clear(self): #clear함수:다 지워버린다. \n",
        "        self._size = 0 # size를 0으로 초기화\n",
        "        self.head.next = self.tail # size가 초기화 되었으므로 head의 다음은 tail\n",
        "        self.head.prev = None # preivous는 아무것도 없다\n",
        "        self.head.next = None # head의 다음도 없다\n",
        "        self.tail.prev = self.head #tail의 이전은 head다\n",
        "\n",
        "    def delete(self, data): #data를 삭제하는 함수\n",
        "        prev = self.head #현재 previous는 헤드이다 왜냐하면 기본 구조인 head-tail이기 때문입니ㅏㄷ.\n",
        "        current = prev.next # current는 Previous의 다음. head - previous - current - tail\n",
        "        while current is not None: #current가 None이 되면 멈춘다.\n",
        "            if current.data == data: # 만약 현재의 data가 data라면\n",
        "                prev.next = current.next #previous는 current의 다음인 next에 할당\n",
        "                current.next.prev = prev # next의 이전은 current가 아닌 previous\n",
        "                current.next = None #next = None\n",
        "                current.prev = None # previous =None\n",
        "                self._size -= 1 # current가 사라졌으므로 사이즈 감소\n",
        "                return True # 이것이 잘 수행되었다면 true \n",
        "\n",
        "            #이 부분이 previous가 current의 삭제로 next로 연결 되었을 때 생기는 변화\n",
        "            prev = prev.next # prev는 current\n",
        "            current = current.next #current 는 previous가 되는 \n",
        "        \n",
        "        return False # 위의 것들이 수행이 안되면 False출력\n",
        "\n",
        "    def delete_by_index(self, index):#index를 사용하여 값 삭제\n",
        "        if index >= self._size or index < 0: #index가 size보다 이상이거나 0보다 작다면\n",
        "            raise RuntimeError(\"Index out of error\") # 인덱스가 범위를 벗어났다는 에러 호출\n",
        "\n",
        "        prev_, current_, next_ = None, None, None # 싹 다 초기화!! 하는 이유는 여러 구현 시도를 하려면 비어 있는 상태가 편합니다. \n",
        "                                                 # 우리가 짐을 쌓기 전에 상자에 불필요한 물건이 없는지 확인 후에 담는 것처럼요\n",
        "\n",
        "        i = 0 # 초기화\n",
        "        if index < self._size // 2: #인덱스가 사이즈의 절반보다 작다면?\n",
        "            prev_ = self.head #prev_의 node 초기화\n",
        "            current_ = self.head.next # node 초기화(헤드 다음 노드 없다)\n",
        "            while i < index: # i가 인덱스보다 이상일 때까지 실행\n",
        "                prev_ = prev_.next #prev는 current가 된다\n",
        "                current_ = current_.next #current는 next가 된다\n",
        "                i += 1 # i 증가 , 하나씩 밀리기 때문\n",
        "            prev_.next = current_.next # next가 동일해짐: head - prev -(current) - next- tail구조\n",
        "            current_.next.prev = prev_ # head - prev -(current) - next- tail구조 이런 구조화\n",
        "            current_.next = None #초기화\n",
        "            current_.prev = None#초기화\n",
        "        else: # 인덱스가 사이즈의 절반보다 이상\n",
        "            current_ = self.tail.prev # 구조: head- prev - current - (next) - tail\n",
        "            next_ = self.tail # 구조: head- prev - current - (next) - tail\n",
        "            while i < (self._size - index -1): # i >= (self._size - index -1)될 떄까지 실행\n",
        "                next_ = next_.prev # next가 사라지니 이전인 current에 적용\n",
        "                current_ = current_.prev # current가 사라지니 이전인 previous적용\n",
        "\n",
        "            next_.prev = current_.prev # next_ = current_\n",
        "            current_.prev.next = next_ # 뒤로 갔다 앞으로 가는 느낌\n",
        "            current_.next = None #초가화\n",
        "            current_.prev = None #초가화\n",
        "        \n",
        "        self._size -= 1 #next가 줄었기에 사이즈 감소\n",
        "        return True #이것이 실행되면 true출력\n",
        "\n",
        "    def get(self, index): #index가 인자인 get 힘수\n",
        "        if index >= self._size or index < 0: # index가 사이즈보다 크거나 0보다 작다면\n",
        "            raise RuntimeError(\"Index out of error\") # 인덱스 범위 에러 호출\n",
        "\n",
        "        i = 0 #i=0으로 초기화\n",
        "        current = None # current도 초기화\n",
        "        if index < self.size //2: # index가 절반보다 이상이라면\n",
        "            current = self.head.next # current는 head의 다음\n",
        "            while i < index: # i가 인덱스보다 작다면\n",
        "                current = current.next #current는 next\n",
        "                i += 1# i는 1 증가\n",
        "        else: #index절반 미만이라면\n",
        "            current = self.head.prev # current가 head전\n",
        "            while i < (self._size - index -1):\n",
        "                current = current.prev # current는 preivious\n",
        "                i += 1 # i는 1 증가\n",
        "\n",
        "        return current.data\n",
        "\n",
        "    def index_of(self, data): #index 증감 함수\n",
        "        current = self.head.next #current가 head의 다음 \n",
        "        index = 0 #index=0으로 초기화\n",
        "        while current != None: # cuurent가 None이 될 때까지 순환\n",
        "            if current.data != None and current.data == data: ##current가 none가 아니고 데이터가 있다면 \n",
        "                return index #index 출력\n",
        "            current = current.next #current가 next라면\n",
        "            index += 1 #인덱스의 위치가 1 증가\n",
        "        return -1 # -1 반환\n",
        "\n",
        "    def is_empty(self): #비어있을 경우 함수\n",
        "        return self.head.next == self.tail #head 다음이 tail\n",
        "\n",
        "    def contains(self, data): #data포함이 되었을 때 함수\n",
        "        current = self.head.next #head다음이 current인 구조 head- current - tail\n",
        "        while current != None: # current가 None일 때까지 구햔\n",
        "            if current.data != None and current.data == data: #current가 none가 아니고 데이터가 있다면 \n",
        "                return True # true출력\n",
        "            current = current.next #current가 next라먄\n",
        "        return False #false 출력\n",
        "\n",
        "    "
      ],
      "metadata": {
        "id": "bvYGfKNr7mxB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#직접 코드를 구현한 DoubleLinkedList에 실제 값을 넣어서 실행시키기\n",
        "\n",
        "if __name__ == \"__main__\": #이 파일의 이름이 main.py일 것이기에 터미널 실행을 위한 것입니다.\n",
        "    l = DoubleLinkedList() # DoubleLinkedList()을 매번 치긴 너무 기니 하나의 문자 l(ist)로 축약\n",
        "    for elem in [3,2,4,1,4]: # [3,2,4,1,4]들이 elem에 하나씩 들어가서 출력 add 함수 구현\n",
        "        print(f'l.add({elem})')\n",
        "        l.add(elem)\n",
        "    print(f\"l.size(): {l.size()}\") #총 size출력, size함수 구현\n",
        "\n",
        "    print(\"======================\") # 줄바꿈\n",
        "    for elem in [3,2,4,1,4,100]: #[3,2,4,1,4,100]에서 하나씩 호출\n",
        "        print(f\"l.contains({elem}): {l.contains(elem)}\") #contains함수 구현\n",
        "        print(f\"l.index_of({elem}): {l.index_of(elem)}\") #idex_of 함수 구현\n",
        "\n",
        "    print(\"=======================\") #줄 바꿈\n",
        "    for elem in [4,5,100]: # [4,5,100]에서 하나씩 출력\n",
        "        print(f\"l.delete({elem}): {l.delete(elem)}\") #delete 함수 구현\n",
        "\n",
        "    print(f\"l.size(): {l.delete(elem)}\") #delete가 잘 되는지 확인\n",
        "\n",
        "    print(f\"l.size(): {l.size()}\") # 사이즈 확인\n",
        "\n",
        "    print(f\"l.insert(0, 100) \") #어느 위치에 insert할지 명시\n",
        "    l.insert(0, 100)\n",
        "    print(f\"l.insert(2,101) :\") # 어느 위치에 insert할지 명시\n",
        "    l.insert(2,101)\n",
        "     \n",
        "    #insert적용하여 숫자를 tail부터 넣음 \n",
        "    for elem in [3,2,4,5,1,4,100,101]: # insert해야 하는 거 추가 후 일일이 빼기\n",
        "        print(f\"l.contains({elem}): {l.contains(elem)}\") # 구현 결과 contains함수 구현\n",
        "        print(f\"l.index_of({elem}): {l.index_of(elem)}\") # index_of 함수 구현"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2yuRGe4D97tv",
        "outputId": "227a1234-93aa-4b01-fe2f-e14dc99d6b07"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "l.add(3)\n",
            "l.add(2)\n",
            "l.add(4)\n",
            "l.add(1)\n",
            "l.add(4)\n",
            "l.size(): 5\n",
            "======================\n",
            "l.contains(3): True\n",
            "l.index_of(3): 0\n",
            "l.contains(2): True\n",
            "l.index_of(2): 1\n",
            "l.contains(4): True\n",
            "l.index_of(4): 2\n",
            "l.contains(1): True\n",
            "l.index_of(1): 3\n",
            "l.contains(4): True\n",
            "l.index_of(4): 2\n",
            "l.contains(100): False\n",
            "l.index_of(100): -1\n",
            "=======================\n",
            "l.delete(4): True\n",
            "l.delete(5): False\n",
            "l.delete(100): False\n",
            "l.size(): False\n",
            "l.size(): 4\n",
            "l.insert(0, 100) \n",
            "l.insert(2,101) :\n",
            "l.contains(3): True\n",
            "l.index_of(3): 1\n",
            "l.contains(2): True\n",
            "l.index_of(2): 3\n",
            "l.contains(4): True\n",
            "l.index_of(4): 5\n",
            "l.contains(5): False\n",
            "l.index_of(5): -1\n",
            "l.contains(1): True\n",
            "l.index_of(1): 4\n",
            "l.contains(4): True\n",
            "l.index_of(4): 5\n",
            "l.contains(100): True\n",
            "l.index_of(100): 0\n",
            "l.contains(101): True\n",
            "l.index_of(101): 2\n"
          ]
        }
      ]
    }
  ]
}