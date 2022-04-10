### 이진 탐색 트리

![](https://velog.velcdn.com/images/qsdcfd/post/1081685b-5180-4ca0-ab7e-482e48cee1a9/image.png)

트리 구조 자체로는 데이터의 특성에 아무런 제약이 없다.

노드의 왼쪽 서브 트리에는 루트 노드보다 작은값이다.

노드의 오르쪽 서브 트리에는 루트 노드보다 큰 값이다.

중복된 값이 없다.

서브 트리는 다시 이진 탐색 트리가 되어서 위의 특징을 갖는다.

레벨에 생각 없이 트리의 가장 왼쪽 값이 최솟값이고 오른쪽 값이 최댓값입니다.


<br>

*삽입

중복된 데이터를 삽입할 경우 삽입이 되지 않습니다.

추가된 노드는 트리의 leaf에 삽입을 합니다.

![](https://velog.velcdn.com/images/qsdcfd/post/be97a198-81b5-42d1-bc58-5e6bf9dfa197/image.png)


*삭제

- 삭제는 세 가지 경우가 있습니다. (삭제 데이터의 위치를 찾음)

   - 삭제할 데이터가 leaf:가장 아래 값을 숫자->null로 바꿔서 해결
   
   -  한 개의 자식 노드를 가질 경우: 삭제할 노드의 부모 와 자식 노드 사이에 넣기
   
   - 두 개의 자식 노드를 가질 경우: 왼쪽 서브 트리의 최댓값과 교채하고 오르쪽 서브 트리의 최솟값과 교체

<br>

*삭제할 데이터가 leaf

![](https://velog.velcdn.com/images/qsdcfd/post/ce449dba-28d1-4185-b1ff-cd528280d241/image.png)

*한 개

![](https://velog.velcdn.com/images/qsdcfd/post/64a49740-f3df-491e-b860-06e4aa187b70/image.png)


*두 개

![](https://velog.velcdn.com/images/qsdcfd/post/522ee9c7-e636-4314-9381-0add78b15577/image.png)

![](https://velog.velcdn.com/images/qsdcfd/post/5a4c8494-e711-4771-81b0-5903509df9c2/image.png)

