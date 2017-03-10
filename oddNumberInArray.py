def solution(A):
    # for num in A:
    #     if A.count(num) == 1:
    #         return num
    d = {}
    for num in A:
        d[num] = d.get(num, 0) + 1
    for key, val in d.items():
        if val%2 != 0:
            return key


print solution([9, 9, 9, 9, 3,3,3,3,3,3,3,3,3,3,3,3,3])
