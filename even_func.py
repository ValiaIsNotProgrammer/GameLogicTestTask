from typing import Union
import time

"""
На языке Python написать алгоритм (функцию) определения четности целого числа, 
который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 

"""
def timer(func):
    def wrapper(value):
        start = time.time()
        for i in range(1,100_000):
            func(i)
        print("Время выполнение функции", func.__name__ , time.time() - start)
    return wrapper

@timer
def is_even_v1(value):
    return value % 2 == 0

@timer
def is_even_v2(num):
    return num >> 1


if __name__ == "__main__":
    for f in (is_even_v1, is_even_v2):
        f(2)
