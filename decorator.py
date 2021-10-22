import time


def deco(func):
    def wrapper(*args,**kwargs):
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


@deco
def a(start, finish):
    return "result"


a(1, 2)


def deco_timing(accuracy):
    def deco_timing_inside(func):
        def wrapper(*args,**kwargs):
            start = time.perf_counter()
            result = func(*args,**kwargs)
            end = time.perf_counter()
            print('Время выполнения: {} секунд.'.format(round(end-start, accuracy)))
            return result
        return wrapper
    return deco_timing_inside


@deco_timing(accuracy=2)
def dream(sec):
    time.sleep(sec)


dream(5)
