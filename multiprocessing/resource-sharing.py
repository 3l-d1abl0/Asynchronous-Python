import multiprocessing

def func(x):
    print(x**x)

if __name__ == "__main__":
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.map(func, [1,2,3])