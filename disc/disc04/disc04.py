#1.1
def count_stairs_ways(n):
    if n == 1:
        return 1
    else:
        return (count_stairs_ways(n - 1) + count_stairs_ways(n - 2))
#1.2 存疑
def count_stair_ways(n, k):
    if n == 1:
        return 1
    else:
        total = 0
        for step in range(1, min(k, n) + 1):
            total += count_stair_ways(n - step, k)
        return total
#2.2
def even_weighted(s):
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]
#2.3
def max_product(s):
    if len(s) == 0:
        return 0 
    elif len(s) == 1:
        return s[0]
    else:
        with_first = s[0] * max_product(s[2:])
        without_first = max_product(s[1:])
        return max(with_first , without_first)