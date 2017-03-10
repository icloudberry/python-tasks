def solution(A, K):
    # write your code in Python 2.7
    if K == 0 or len(A) == 0:
        return A
    shifts = K % len(A)
    res1 = [x for x in A[:-shifts:1]]
    res2 = [x for x in A[-shifts::1]]
    return res2+res1


print solution([0,1,2,3],1)
print solution([0,1,2,3],2)
print solution([0,1,2,3],3)
print solution([0,1,2,3],6)
print solution([0,1,2,3],0)
