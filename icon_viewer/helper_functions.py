# gets divisors of one num
def get_divisors(x):
    result = []

    # start at 1 because dividing through 0 is undefined
    for i in range (1, x + 1):
        if (x % i == 0):
            result.append(i)
    return result

# gets common divisors of two nums
def get_common_divisors(x, y):
    result = []

    # determining which one is the bigger num
    smaller = x
    bigger = y

    if x > y:
        smaller = y
        bigger = x

    # start at 1 because dividing through 0 is undefined
    for i in range (1, smaller + 1):
        if (bigger % i == 0) & (smaller % i == 0):
            result.append(i)
    return result