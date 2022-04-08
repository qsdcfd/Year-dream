
### Quick Sort

병합 정렬처럼 숫자를 나누면서 정렬이 진행이 되기에 시간복잡도는 O(NlogN)이 됩니다.

하지만 시간은 병렬 정렬보다 빠릅니다.

**특징**

#### 참조지역성(locality of reference)

공간(spaital)지역성: 특정 클러스터의 기억 장소들에 대해 참조가 집중적으로 이뤄지는 경향으로 참조된 메모리 근처의 메모리를 참조합니다.
   
시간(temporal)지역성: 최근 사용된 기억 장소들에 집중적으로 엑세스가 되는 경향으로 참조했던 메모리는 빠른 시간에 다시 참조될 확률이 높다
   
순차(sequential)지역성: 데이터가 순차적으로 엑세스되는 경향으로 명령어가 순차적으로 구성이 되어있습니다.
   
 <br>
 
한 번 결정된 pivot값은 이후의 연산에서 제외가 되기에 빠릅니다.(데이터의 수가 줄어듭니다) 그리고,
pivot의 인덱스는 바뀔 수 있고 pivot기준으로 왼쪽은 작은 값 이고 오른쪽은 큰 값입니다.
 

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/e0101eda-62a8-4b4f-9055-de4a170f9b00/public)

서브 리스트에서도 위에 했던 과정을 반복합니다.

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/ff74ac38-0e4f-4b75-f6ed-9a22bc948300/public)

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/b44db368-7a3b-47f2-2846-246b9e898f00/public)


추가적인 메모리 사용 공간이 없습니다
   
한 번만 접근하고 나면 캐싱메모리로 처리하기에 추가 사용이 필요없습니다.
 
불안정 정렬입니다.

*시간복잡도

평균: O(NlogN)

최악은 정렬된 리스트:O(N^2)

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/118dc1f3-70c0-4198-eb73-c0aff70e7200/public)
