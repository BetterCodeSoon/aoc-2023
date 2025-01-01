import time


def benchmark(func) -> any:
    t1 = time.perf_counter()
    value = func()
    t2 = time.perf_counter()
    print(f"\nFinished {func.__name__} in {t2 - t1} seconds.\n")
    return value


def benchmark(func, *args) -> any:
    t1 = time.perf_counter()
    value = func(*args)
    t2 = time.perf_counter()
    print(f"\nFinished {func.__name__} in {t2 - t1} seconds.\n")
    return value
