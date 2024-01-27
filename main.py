from time import time


def factorize(lst: list) -> list:
    res = []
    for i in lst:
        j = 1
        while j <= i:
            if i % j == 0:
                res.append(j)
            j += 1
    return res


start_time = time()
print(factorize([5126531, 32541516]))
print(f'{round(time() - start_time, 4)} sec')