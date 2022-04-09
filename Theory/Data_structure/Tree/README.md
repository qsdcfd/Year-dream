## 기초 트리 개념

### 트리

한 노드가 여러 노드를 가르킬 수 있는 것으로 비선형적 자료구조입니다. 

그리고, 데이터 구조의 계층적인 속성을 표현하고 그래프 형태입니다.

*root와 edge

![](https://velog.velcdn.com/images/qsdcfd/post/deed5b2b-6051-4463-addc-69a397d0f7e3/image.png)

*부모 자식
![](https://velog.velcdn.com/images/qsdcfd/post/c40aa3b5-9d03-4c6b-b0ab-9906f7905fb6/image.png)

*경로(path)

![](https://velog.velcdn.com/images/qsdcfd/post/c0d55330-5798-4a82-b365-1ebc246ffe1d/image.png)

*Depth

![](https://velog.velcdn.com/images/qsdcfd/post/cf08c351-5b64-49dc-a9f4-9c903ff1287e/image.png)

*level

![](https://velog.velcdn.com/images/qsdcfd/post/129c8da0-8fd9-4948-8c91-7114a5b8aed8/image.png)

*트리 안에 서브 트리(재귀적 관점)

![](https://velog.velcdn.com/images/qsdcfd/post/f437b736-3eef-4ea3-a7e2-532a50d2c5c0/image.png)


*현실 예시

![](https://velog.velcdn.com/images/qsdcfd/post/4df58eb7-5160-46e7-8eb0-c90a91369552/image.png)

*종류

이진 트리

AVL 트리, 레드-블랙 트리

B-트리, B+트리

세그먼트 트리

트라이

<br>

### 이진 트리

각 노드가 최대 2개(0~2)의 자식 노드를 가지는 트리이지만 왼쪽 자식노드와 오른쪽 자신노드와 다릅니다.

![](https://velog.velcdn.com/images/qsdcfd/post/4066289f-d064-4f30-af22-7a73eeb616bf/image.png)

*간단한 코드

```
class Node {
    int data;
    Node left;
    Node right;
}
```


**정 이진 트리(full binary tree, strict tree)**

모든 노드가 2개의 자식을 가지거나 자식이 없는 경우를 말합니다.

![](https://velog.velcdn.com/images/qsdcfd/post/c74e087d-6ffa-41a7-813a-0ec94bbb4b89/image.png)

<br>

**포화 이진 트리(Perfect Binary Tree)**

모든 노드가 2개의 자식을 가지고 leaf노드가 같은 레벨

높이가 h인 포화 이진 트리에서 노드 갯수는 2^(k+1) -1

Leaf 노드의 갯수는 2^h

![](https://velog.velcdn.com/images/qsdcfd/post/16a286d0-b3f7-4e87-9853-52abda2aa2a3/image.png)

<br>

**완전 이진 트리(Complete Binary Tree)**

마지막 레벨을 제외하고 모든 노드가 채워져하고 이때 노드는 왼쪽에서 오른쪽으로 채워집니다.

![](https://velog.velcdn.com/images/qsdcfd/post/be19c091-a837-4133-a7a3-f80dfb3dee99/image.png)

이러한 특성으로 일차원 배열로 표현이 가능합니다.

![](https://velog.velcdn.com/images/qsdcfd/post/3d0e4b5a-dd0e-49fa-9cfe-c4ffd9e774c2/image.png)

<br>

**이진 트리의 응용**

힙

이진 탐색 트리(Binary Search Tree)

B-tree

AVL트리

<br>

**이진 트리의 기본 연산**

트리에 데이터 삽입, 삭제, 검색 그리고 탐색까지 합니다.

<br>

### 트리 순회(루트 노드 방문의 차이로 나눠짐)

![](https://velog.velcdn.com/images/qsdcfd/post/1220f409-d6c5-4b4b-94d6-61dfe72cccd6/image.png)

![](https://velog.velcdn.com/images/qsdcfd/post/14edb6b6-c601-4c3a-89a2-e62f6e69c813/image.png)

#### 전위 탐색(preorder)

루트 노드를 방문하고 왼쪽 서브 트리를 그리고 오른쪽 서브 트리를 합니다.

![](https://velog.velcdn.com/images/qsdcfd/post/b5759bb7-3c6f-47ed-bb05-1c3a955c88f1/image.png)

<br>

#### 중위 탐색(inorder)

왼쪽 서브 트리 후 루트 노드 방문하고 마지막으로 오른쪽 서브 트리를 합니다.

![](https://velog.velcdn.com/images/qsdcfd/post/23979188-60ed-4485-8d46-c4ad4dc6d5a2/image.png)


<br>

#### 후위 탐색(postorder)


왼쪽 서브 트리 후 오른쪽 서브 트리를 하고 마지막에 (루트)노드 방문합니다.

![](https://velog.velcdn.com/images/qsdcfd/post/ff5a1bd5-6e5a-4ef2-a44e-e265ceaab4ff/image.png)


