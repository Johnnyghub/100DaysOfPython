import time


def speed_calc_decorator(function):
    def wrapped_function():
        current_time = time.time()
        function()
        finish_time = time.time()
        elapsed_time = finish_time - current_time
        print(f"Elapsed time for {function.__name__}: {elapsed_time}")
    return wrapped_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i  # just so the loop does something, ignore orange line the code came like this


@speed_calc_decorator
def slow_function():
    for i in range(100000000):  # this has 1 more zero, don't be confused
        i * i


fast_function()
slow_function()
