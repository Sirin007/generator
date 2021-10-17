import time


def deco(func):
    def wrapper(*args):
        for x in args:
            print(x)
        print(func(*args))
    return wrapper


@deco
def a(start, finish):
    return "result"


a(1, 2)


def deco_timing(func):

    def wrapper(param, accuracy):
        start = time.perf_counter()
        func(param)
        end = time.perf_counter()
        print('Время выполнения: {} секунд.'.format(round(end-start, accuracy)))
    return wrapper


@deco_timing
def dream(sec):
    time.sleep(sec)


dream(5, 10)
