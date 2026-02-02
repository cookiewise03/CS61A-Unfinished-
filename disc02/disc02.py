#questions
#1.1
def keep_ints(cond ,n):
    for i in range(1 , n+1):
        if cond(i):
            print(i)
def is_even(x):
        return x % 2 == 0
keep_ints(is_even ,5)
#1.2
def make_keeper(n):
    def keep_ints(cond):
        for i in range(1 , n+1):
            if cond(i):
                print(i)
    return keep_ints
make_keeper(5)(is_even)
#1.7 延迟打印，保存参数等下一次调用时使用
def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print
#1.8
def print_n(n):
    def inner_print(x):
        if n <=0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print