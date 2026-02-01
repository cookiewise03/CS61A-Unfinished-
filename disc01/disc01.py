def wear_jacket_withif(temp, rain):
    if temp < 60 or rain:
        return True
    else:
        return False

def wear_jacket_withoutif(temp, rain):
    return temp < 60 or rain

def is_prime(n):
    if n <= 1:
        return False
    i= 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True