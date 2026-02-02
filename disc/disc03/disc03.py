#question 
#1.1
def multiply(m , n):
    if m < n :
        m , n = n , m
    if n == 0 :
        return 0
    else :
        return m + multiply(m , n - 1)
#1.3
def hailston(n):
    i = 0
    if n <= 0 :
        return None
    elif n == 1 :
        print(n)
        i += 1
        return i
    elif n % 2 == 0 :
        print(n)
        i += 1
        return hailston(n // 2)
    elif n % 2 == 1 :   
        print(n)
        i += 1
        return hailston(3 * n + 1)
#1.4
def merge(n1, n2):
    if n1 < 0 or n2 < 0:
        return -1
    elif n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + (n1 % 10)
    else:
        return merge(n1, n2 // 10) * 10 + (n2 % 10)
#1.5
def make_func_repeater(f, x):
    def repeat(i):
        if i <= 1:
            return f(x)
        else:
            return f(repeat(i - 1))
    return repeat
#1.6
def is_prime(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True
def is_prime(n):
    def prime_helper(k):
        if k == 1:
            return False
        elif n % k == 0:
            return False
        else:
            return prime_helper(k - 1)
    return prime_helper(n - 1)  
