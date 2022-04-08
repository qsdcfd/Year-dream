{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Hash",
      "provenance": [],
      "authorship_tag": "ABX9TyMZ67QZWN1mlKocr85QyM7n"
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
        "id": "TjWTXOafptfF"
      },
      "outputs": [],
      "source": [
        "class Node: #Node는 딕셔너리 구조의 키와 value값을 가지는 구조입니다.\n",
        "    def __init__(self, key, val): #클래스의 인자로 key와 value구하기\n",
        "        self.key = key #keu 힐딩\n",
        "        self.value = val #value할당"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class HashTable: #해시 테이블 클래스 만들기\n",
        "    def __init__(self, bucket_size=1024): #버킷 사이즈 설정\n",
        "        self.buckets = [[]] * bucket_size #빈 리스트에 사이즈를 곱해서 버킷 만들기\n",
        "        self.bucket_size = bucket_size #버킷 사이즈 할당\n",
        "        self._size = 0 #초기 사이즈는0으로 초기화\n",
        "\n",
        "    \n",
        "    def put(self, key, val): #넣기\n",
        "        idx = hash(key) % self.bucket_size #인덱스는 해쉬의 키 %1024의 몫\n",
        "        for elem in self.buckets[idx]: #인덱스 추출\n",
        "            if elem.key == key: # 나오는 값에 맞게 key설정\n",
        "                elem.val == val # value설정\n",
        "                return\n",
        "            node = Node(key, val) #node는 키와 value의 딕셔너리 구조\n",
        "            self.buckets[idx].append(node) # 노드 삽입\n",
        "            self._size += 1 #사이즈 1 증가\n",
        "\n",
        "\n",
        "    def get(self, key): #key값 얻기\n",
        "        idx = hash(key) % self.bucket_size #몫이 곧 인덱스\n",
        "        for elem in self.buckets[idx]: #인덱스를 순차적으로 뽑기\n",
        "            if elem.key == key: #key값이 동일하다면\n",
        "                return elem.val #value 반환\n",
        "        return None #아니라면 비어있는 거\n",
        "\n",
        "    \n",
        "    def contains(self, key): #버킷에 key값이 있는지 확인\n",
        "        idx = hash(key) % self.bucket_size #몫을 통해서 인덱스 구하기\n",
        "        for elem in self.buckets[idx]: #인덱스 추출\n",
        "            if elem.key == key: #같다면\n",
        "                return True#true반환\n",
        "        return False#아니면 false\n",
        "\n",
        "    def delete(self, key): #삭제함수\n",
        "        idx = hash(key) % self.bucket_size #인덱스 몫 추출\n",
        "        for idx, elem in enumerate(self.buckets[idx]):#해당 인덱스의 키와 값 동시 추출\n",
        "            if elem.key == key: #같다면\n",
        "                self.buckets[idx].remove(elem) #버킷의 인덱스와 값 소멸\n",
        "                self._size -= 1 #사이즈가 줄어든다\n",
        "\n",
        "    def size(self):#사이즈 함수\n",
        "        return self._size #사이즈를 반환한다.\n",
        "    "
      ],
      "metadata": {
        "id": "HQfpRHFi3B6y"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == \"__main__\": #main.py\n",
        "    table = HashTable() #table은 클래스 HashTable할당\n",
        "\n",
        "    #put함수 구현\n",
        "    print('table.put(\"s1\", \"v1\")') #키인 s1, 값인 v1추출\n",
        "    table.put(\"s1\",\"v1\") #키인 s1, 값인 v1 넣기\n",
        "    print('table.put(\"s2\",\"v2\")') #키인 s2, 값인 v2추출\n",
        "    table.put(\"s2\",\"v2\") #키인 s2, 값인 v2넣기\n",
        "    print('table.put(\"s3\",\"v3\")')#키인 s3, 값인 v3 추출\n",
        "    table.put(\"s3\",\"v3\") #키인 s3, 값인 v3 넣기\n",
        "   \n",
        "\n",
        "    print(f\"table.size(): {table.get('s1')}\") #s1의 사이즈 구해라\n",
        "   \n",
        "    print(f\"table.get('s1'): {table.get('s1')}\")\n",
        "    print(f\"table.get('s2'): {table.get('s2')}\")\n",
        "    print(f\"table.get('s3'): {table.get('s3')}\")\n",
        "   \n",
        "    print(\"table.put('s2', 'v4')\") #키인 s2, 값인 41추출\n",
        "    table.put(\"s2\", \"v4\") #키인 s2, 값인 v4 추출\n",
        "   \n",
        "    print(f\"table.get('s2'): {table.get('s2')}\") #get함수 구현\n",
        "   \n",
        "    print(\"table.delete('s2')\")  # s2 삭제해라\n",
        "   \n",
        "    print(f\"table.size(): {table.size()}\") #길이 구하기\n",
        "   \n",
        "    print(f\"table.get('s1') :{table.get('s1')}\")#get함수 구현\n",
        "    print(f\"table.get('s2') :{table.get('s2')}\")#get함수 구현\n",
        "    print(f\"table.get('s3') :{table.get('s3')}\")#get함수 구현"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v2nRAdAp4ml2",
        "outputId": "bcc3a817-a624-4793-f066-e14488353d8a"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "table.put(\"s1\", \"v1\")\n",
            "table.put(\"s2\",\"v2\")\n",
            "table.put(\"s3\",\"v3\")\n",
            "table.size(): None\n",
            "table.get('s1'): None\n",
            "table.get('s2'): None\n",
            "table.get('s3'): None\n",
            "table.put('s2', 'v4')\n",
            "table.get('s2'): None\n",
            "table.delete('s2')\n",
            "None\n",
            "table.size(): 0\n",
            "table.get('s1') :None\n",
            "table.get('s2') :None\n",
            "table.get('s3') :None\n"
          ]
        }
      ]
    }
  ]
}