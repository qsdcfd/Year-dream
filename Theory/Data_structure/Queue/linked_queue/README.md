### linked_queue

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/12ae9d76-ebda-4d55-3d0c-8aa109be5300/public)



Linked List는 노드들이 위와 같이 여러 구조로 연결한 것입니다.

#### 활용

*삽입

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/df18ba80-799b-4ae3-3c30-0ec1399f4e00/public)


자료를 삽입하려면 추가할 장소로 가서 기존의 링크를 끊은 후에 추가할 위치의 prev와 next를 연결하는 힙니다. 시간 복잡도는 다이렉트이기에 O(1)입니다.

*제거

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/55862924-66c3-4a81-3963-653e34c31200/public)

자료를 삭제하려면 삭제 하고 싶은 부분의 prev와 next를 연결시키면 되고 이것 또한 O(1)입니다.

*자료 검색

자료를 검색하려면 맨 앞 부분인 head부터 tail까지 가야하므로 노드를 순차적으로 검색하고 시간 복잡도는 O(n)입니다.
