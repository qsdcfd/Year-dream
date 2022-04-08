### Circular_queue

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/c638a82c-bff4-41ba-cf80-51a951a60900/public)

배열로 구현이 되지만 배열의 단점을 극복한 것입니다. 

원형 큐 또한 큐이기 때문에 선입선출방식입니다.

고정된 크기의 배열로 구현되고 원이기 때문에 수열적 생각도 좋습니다.

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/b8a2eb2e-61f9-4345-eb49-be6eb704c400/public)


#### 활용

*삽입

데이터가 처음 삽입될 때 rear방향으로 삽입됩니다.

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/43698ae5-31d8-49f9-3e2a-80b6a2496e00/public)

데이터가 끝 위치에 다닿으면 다음에는 다시 처음인 0번째 인덱스부터 쌓습니다.

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/d1aecb42-4a01-4ae0-7d76-8ebfe3839900/public)

*추출

데이터를 추출할 때도 front방향으로 하나씩 추출됩니다.

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/78b9b60c-3fc0-4abe-e74d-d94e998e5000/public)

*원형 큐의 꽉찬 상태

하나 남은 상태에서 front = rear + 1이라면 꽉찬 상태입니다.

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/ce527546-638d-42d1-2b47-429583253000/public)


*메서드

isFull() :꽉 찬 상태

isEmnpty(): 비어있는 상태
