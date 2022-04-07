### Double_linked_list

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/0f875e8d-25d6-43e7-9a3e-773455f07200/public)


단일 연결 리스트와 달리 head와 tail를 가지고 각 노드는 앞 과 뒤 노드의 정보를 가지고 있기에 양쪽으로 접근이 가능합니다. 그래서 양방향 연결 리스트라고 불리게 되었습니다.

<br>

#### 활용

*삽입

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/97632137-9bf8-46a6-9966-e9e75ba21400/public)


삽입할 노드(new_node)의 prev는 이전 노드를 가리킵니다.

삽입할 노드의 다음은 삽입할 노드의 뒤 노드를 가리킵니다.

뒤의 노드 prev가 삽입할 노드를 가리키고 앞 노드의 next 또한 삽입 노드를 가리킵니다.

양방향 연길 리시트는 오른차순으로 구성되는 것을 베이스로 깝니다.

특정 노드를 기준으로 데이터를 삽입하는 것 또한 순서는 동일합니다.

<br>

*삭제

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/4aeeba82-5e88-4f92-6876-a4a23decf100/public)

첫 노드를 제거한다고 생각을 해야합니다(헤드 삭제X)

헤드의 NEXT가 삭제할 노드의 뒷 노드를 가리키고 뒷 노드의 prev는 헤드를 가리킵니다.

삭제할 노드 메모리 해제

특정 노드 삭제

삭제할 노드가 유일한 노드인 경우

삭제할 노드가 Head인 경우

삭제할 노드가 Tail인 경우

삭제할 노드가 일반 노드인 경우

