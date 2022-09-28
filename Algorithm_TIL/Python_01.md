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
