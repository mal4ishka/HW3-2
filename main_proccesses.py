from time import time
from multiprocessing import Pool, cpu_count


def factorize(el: int) -> list:
    res = []
    j = 1
    while j <= el:
        if el % j == 0:
            res.append(j)
        j += 1
    return res


if __name__ == '__main__':
    start_time = time()
    l = [5126531, 32541516]
    with Pool(cpu_count()) as pool:
        p = pool.map(factorize, l)
        print(p)
    pool.close()
    pool.join()
    print(f'{round(time() - start_time, 4)} sec')
