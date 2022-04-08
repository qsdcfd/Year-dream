
### Insertion Sort(stabl sort)


리스트의 앞에서부터 이미 정렬된 서브 리스트 값들과 비교 후에 자신의 위치에 삽입을 하는 것입니다.

삽입 정렬은 인덱스 0인 부분(서브 리스트)은 이미 정렬이 되었다고 판단을 하여 인덱스 1인부분 부터 정렬을 시작합니다.

작은 값은 큰 값의 앞으로 보내지고 큰 값은 다른 큰 값이 나오기 전까지 그 위치에서 고정이 된 상태를 말합니다.

그러므로, 데이터의 이동이 많지만 리스트 내의 데이터가 어느정도 정렬이 되어있을 경우는 데이터의 이동이 적습니다.

시간복잡도는 평균적으로은 O(N^2)이지만 최선의 경우(모두 정렬)에는 O(N)이고 최악의 경우(역정렬상태)라면 O(N^2)입니다.

*예시

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/33497a41-038c-48a1-c844-455c6220fc00/public)

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/e34809b9-927a-4092-f77d-2d1030be4300/public)

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/41e551ce-d76b-4c9c-5e86-bd63e3ba8200/public)
