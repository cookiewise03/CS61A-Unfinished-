#1.1
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n 
        n = g(n)
        return n
    return f
#2.3
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for e in s:
        key = fn(e)
        if key in grouped:
            grouped[key].append(e)#当值为列表时可以这么写
        else:
           grouped[key] = e
    return grouped
#2.4
def add_this_many(x, el, s):
    """ 在列表末尾添加与s中x出现次数相同的el
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    count = 0
    for item in s:
        if item == x:
            count += 1
    for _ in range(count):
        s.append(el)
#4.1
def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even))  # 将filter调用产出的值转为列表
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for e in iterable:
        if fn(e):
            yield e
#4.2
def merge(a, b):
    """
    >>> def sequence(start, step):
            while True:
                yield start
                start += step
    >>> a = sequence(2, 3)  # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2)  # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b)  # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    a_next, b_next = next(a), next(b)
    while True:
        if a_next < b_next:
            yield a_next
            a_next = next(a)
        elif a_next > b_next:
            yield b_next
            b_next = next(b)
        else: 
            yield a_next
            a_next, b_next = next(a), next(b)