
### Hash

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/448f0633-3ffe-4098-b9e2-1941a5e81400/public)


KEY: 중복이 되지 않는 고유 값

VALUE : Key를 기준으로 매핑됨

Hash 함수: key와 value관계를 성공적으로 만들어주는 것. 즉, 키를 통해서 해시값을 매핑시키는 함수입니다.

시간복잡도는 O(1)

해싱함수가 좋다면 키 값을 고르게 분포시키기에 계산이 빠르고 충돌을 최소화 시킵니다.

<br>

*Hashing

데이터를 빠르게 저장하고 가져오는 기법 중 하나로 키에 특정 연산을 적용하여 테이블의 주소를 계산하는 것을 말합니다.

*해시 테이블

순서가 존재하지않고 (KEY,VALUE)구조를 가집니다.

<br>

### 해시 충돌

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/f83f5ee7-6018-41da-7e78-d30e901e6600/public)

키 값이 다른데, 해시 함수의 결과값이 동일한 경우를 말합니다.


인덱스의 일정 비율 이상의 데이터만 채워져도 충돌 확률은 높아집니다.

<br>

#### 예시

*비둘기 집 원리

N + 1개의 물건을 N개의 상자에 넣는다면 적어도 어느 한 상자에는 두 개 이상의 물건이 들어있다

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/e44ba074-286f-4d43-514c-304fd0e05200/public)


*Birthday Problem

임의의 사람 N명이 모였을 때 그 중에서 생일이 같은 두 명이 존재할 확률은?

생일의 가능한 가짓수는 366개(with 02.29)입니다.

그러나 실제로는 23명만 나와도 절반 이상의 확률, 50명이 만나면 97%확률로 생일이 같은 사람이 나오게 됩니다.


<br>

#### 해결방안

*Chaining

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/280409d1-21b2-47b8-0eb6-bc78493eba00/public)

Bucket으로 연결하여 Value값을 넣는 행위를 말하고 이것이 반복되면 사슬과 같다고 하여 이름이 불리게 됩니다.

+) 도식화

![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/9996cad2-07d5-4346-fe55-960a8c140c00/public)

+) 단점은 시간복잡도가 커져서 O(N)이 걸립니다.

<br>

*Open Addressing

- 선형탐색 방식

   - 해시 충돌 n칸을 건넌 후 다음 버킷에 저장하는 형태로 계산은 단순합니다.
   
   - 대신, 검색 시간이 오래 걸리고 특정 위치에만 몰리게 되는 현상이 생깁니다.(clustering)
   
   
![](https://imagedelivery.net/v7-TZByhOiJbNM9RaUdzSA/056aed16-5811-4fb7-9bce-5c0e12143300/public)


<br>

- 제곱탐색

   - clustering문제를 해결하기 위해 만든 것으로 N^2칸을 건너뛴 버킷에 데이터를 저장합니다.
   
   - 데이터들이 특정 위치에 밀집하는 문제를 해결
   
   - 그러나 처음 해시 값이 같다면 여전히 clustering 문제를 갖고 있습니다.
   
   
<br>

- 이중 해시

   - 해시 값에 다른 해시 함수를 한 번 더 적용한 것으로 최초 해시 값이 같더라도 이동 폭이 다르게 되어서 clustering문제 해결
   
   - Hashfunction1():최초의 해시 값을 구함
   
   - Hashfunction2():  충돌 발생시 이동 폭을 구함
