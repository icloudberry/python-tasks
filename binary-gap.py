def solution(N):
    # write your code in Python 2.7
    bin_str = bin(N)

    max_val = 0
    count = 0
    i = 0
    for c in bin_str:
        if c == '1' and i == 0:
            # the first 1 on the way
            i = count
        elif c == '1' and i > 0:
            # not the first 1, trying to 'close' gap
            max_val = max(max_val, count - i - 1)
            i = count
        count += 1
    return max_val


print solution(9)
