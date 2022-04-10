
### 힙(Heap)

![](https://velog.velcdn.com/images/qsdcfd/post/db62647e-ff20-4c40-b37f-d13c535a22ac/image.png)


완전 이진 트리

최대 힙: 부모 노드의 값은 항상 자식 노드보다 크거나 같기에 루트 노드는 트리의 최댓값입니다.

최소 힙: 부모 노드의 값은 항상 자식 노드보다 작거나 같기에 루트 노드는 트리의 최솟값입니다.

최대/최소를 기준으로 데이터를 찾는 연산을 빠르게 할 수 있다 O(1)

삽입: O(logN)

삭제 O(logN)

<br>

### 활용

**우선순위 큐**

데이터가 들어온 순서에 상관없이 우선순위가 높은 데이터 순으로 처리가 되기에 OS의 작업 스케줄링할 때 사용이 됩니다.

<br>

**힙 정렬**

힙 자료구조의 특성을 이용한 정렬 방법

![](https://velog.velcdn.com/images/qsdcfd/post/7a5fc7bd-b12b-48d7-9794-6768270e1803/image.png)

<br>

**배열로 표현하기**


완전 이진 트리이기 때문에 빈 값이 없는 일차원 배열로 표현이 가능

![](https://velog.velcdn.com/images/qsdcfd/post/ea75bb8a-2b2b-4c54-8d34-dda230723152/image.png)


<br>

**Heapify**

힙의 재구조화로 데이터 추가/삭제 후에도 힙의 속성을 유지합니다.

i) 데이터 1삽입(최솟값)

![](https://velog.velcdn.com/images/qsdcfd/post/43beb66b-ee22-4c7f-b703-24241cc17896/image.png)


- 완전 이진 트리의 형태를 유지해야하므로 우선 leaf노드에 삽입

- 힙의 조건을 만족하는지 확인

- 삽입된 노드와 부모 노드의 값을 바뀜

<br>

ii) 데이터 9삭제 (최댓값)

![](https://velog.velcdn.com/images/qsdcfd/post/25ad4e8a-cb5e-44c1-b9ff-766232327152/image.png)

- 마지막 노드를 루트 노드로 가져온다

- 힙의 조건을 만족하는지 확인

- 자식 노드와 위치를 바꿈
