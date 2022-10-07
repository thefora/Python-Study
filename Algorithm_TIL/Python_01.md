## List Comprehension
<br/>

> 리스트 컴프리헨션(List Comprehension)이란 Python에서 직관적으로 리스트를 생성하는 방법이다. <br/>
> - 직관적이며 간결하기 때문에 리스트를 생성할 때 유용하게 사용할 수 있다.


#### 사용법

```python
[i for i in range(5)]
# [0, 1, 2, 3, 4]

[i for i in range(10) if i%2==1]
# [1, 3, 5, 7, 9]
```

#### 2차원 리스트 초기화

```python
# N x M 리스트 초기화1 (각 요소 0 할당)
[[0] * M for _ in range(N)]

# N x M 리스트 초기화2 (각 요소에 1 ~ N x M 의 값을 순차적으로 할당)
[[1 + j + i * M for j in range(M)] for i in range(N)]
```

<br/><br/><br/>
## Lambda Fucntion
<br>

> 람다 함수(Lambda Fucntion)란 Python에서 사용되는 익명의 함수이다. <br/>
> 함수를 간단하게 작성할 수 있다.

```python
x = lambda a: a + 10
# 함수 이름 : x
# 매개변수 : a
# 반환 값 : a + 10

x(1)
# 11

# 람다 함수를 인수로 사용하는 예시
list(map(lambda x: x + 10, [1, 2, 3]))
# [11, 12, 13]


# 리스트 정렬 예시
a = [(1, 4), (5, 2), (1, 3), (3, 4), (5, 0), (2, 2), (6, 1)]

b = sorted(a)
# [(1, 3), (1, 4), (2, 2), (3, 4), (5, 0), (5, 2), (6, 1)]

c = sorted(a, key = lambda x : x[0]) 
# [(1, 4), (1, 3), (2, 2), (3, 4), (5, 2), (5, 0), (6, 1)]

d = sorted(a, key = lambda x : x[1])
# [(5, 0), (6, 1), (5, 2), (2, 2), (1, 3), (1, 4), (3, 4)]

e = sorted(a, key = lambda x : (x[0], -x[1])) 
# [(1, 4), (1, 3), (2, 2), (3, 4), (5, 2), (5, 0), (6, 1)]

f = sorted(a, key = lambda x : -x[0]) 
# [(6, 1), (5, 2), (5, 0), (3, 4), (2, 2), (1, 4), (1, 3)]

s = ['2 A', '1 B', '4 C', '1 A']
s = sorted(s, key=lambda x: (x.split()[1], x.split()[0]))
# ['1 A', '2 A', '1 B', '4 C']

# 
list_ = [12, 8, 4, 11, 3, 7, 9, 8, 15, 10]
result = list(filter(lambda x : x > 3 and x < 9, list_))
# [8, 4, 7, 8] : boolean 값이 True 라면 반환

```

<br/><br/><br/>
## bissect
<br>

> 이진검색 모듈 <br/>
> bisect_left() : 해당 값의 첫번째 인덱스를 반환 <br/>
> bisect_left() : 해당 값의 마지막 인덱스의 다음 값의 인덱스를 반환

```python
from bisect import bisect_left, bisect_right

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 7
print(bisect_left(nums, n))
# 7
print(bisect_right(nums, n)) 
# 8

nums = [3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7]

n = 4
print(bisect_left(nums, n))
# 1
print(bisect_right(nums, n))
# 3

n = 5
print(bisect_left(nums, n))
# 3
print(bisect_right(nums, n))
# 6

n = 6
print(bisect_left(nums, n))
# 6
print(bisect_right(nums, n))
# 10

# bisect_right() - bisect_left() : 해당 원소의 개수를 나타낸다.

```
