import typing, time, functools

def timeit[**P, T](func: typing.Callable[P, T]) -> typing.Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start = time.time()

        ret = func(*args, **kwargs)
        
        print(f"TIME for {func.__name__!r} -- {(time.time() - start) * 1000 :.5f}ms")

        return ret

    return wrapper

def timeit_sec[**P, T](func: typing.Callable[P, T]) -> typing.Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start = time.time()

        ret = func(*args, **kwargs)
        
        print(f"TIME for {func.__name__!r} -- {(time.time() - start) :.5f}s")

        return ret

    return wrapper

def track_io[**P, T](func: typing.Callable[P, T]) -> typing.Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"TRACK input for {func.__name__!r} -- {args} {kwargs}")
        
        ret = func(*args, **kwargs)

        print(f"TRACK output for {func.__name__!r} -- {ret}")

        return ret
    
    return wrapper
