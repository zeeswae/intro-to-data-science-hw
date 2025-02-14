import time
import functools 

def decorator_1(func):
    @functools.wraps(func)  
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() 
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} sec")
        return result
    return wrapper
