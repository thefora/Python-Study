from bisect import bisect_left, bisect_right

def solution(N, stages):
    stages.sort()
    max_ = stages[-1]
    cal = []
    dic = {}
    for i in range(1, N+1):
        mom = bisect_right(stages, max_) - bisect_left(stages, i)
        son = bisect_right(stages, i) - bisect_left(stages, i)
        dic[i] = son / mom if mom else son / ((N+1)-i)
            
    dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    
    result = []
    for i in dic:
        for j in range(1):
            result.append(i[j])
        
    return result
