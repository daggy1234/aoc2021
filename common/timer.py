import time
import functools

def timer(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> float:
        time_list = []
        for i in range(10):
            start = time.perf_counter()
            function(*args, **kwargs)
            end = time.perf_counter()
            time_list.append(end - start)
            i += 0
        return sum(time_list) / len(time_list) * 1000

    return wrapper