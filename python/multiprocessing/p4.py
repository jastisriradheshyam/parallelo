import time
from multiprocessing import Pool

def sum_square(numbers):
    """Return the sum of squares"""
    s = 0
    for i in range(numbers):
        s+= i*1
    return s

def sum_square_with_mp(numbers):
    """sum of squares with multiprocessing"""
    start_time = time.time()
    p = Pool()
    result = p.map(sum_square, numbers)

    p.close()
    p.join()

    end_time = time.time() - start_time
    print(f"Processing {len(numbers)} numbers took {end_time} time using multiprocessing")

def sum_square_no_mp(numbers):
    """sum of squares without multiprocessing"""
    start_time = time.time()
    result = []
    for i in numbers:
        result.append(sum_square(i))
    end_time = time.time() - start_time
    print(f"Processing {len(numbers)} numbers took {end_time} time using without multiprocessing")

if __name__ == '__main__':
    numbers = range(10000)
    sum_square_with_mp(numbers)
    sum_square_no_mp(numbers)