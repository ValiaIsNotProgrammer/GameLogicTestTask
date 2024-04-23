"""
На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
Объяснить, почему вы считаете, что функция соответствует заданным критериям.
"""


"""
    https://github.com/python/cpython/blob/master/Objects/listobject.c - я моментами использовал референс, 
    так как ни разу не реализовывал этот подход. На литкоде не попадалась мне эта задача,
     поэтому это будет мой первый раз реализации данного алгоритма на Python.
     Т.к. это комбинация двух классических алгоритмов (слияния и вставки), то внимание уделю именно timsort'у
"""
import random
import time



def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

    return arr


def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])


def tim_sort(arr):
    """
    Мы минимальный размер подмассива для сортировки вставками.
    Далее мы делаем сортировка вставками для каждого подмассива длины min_run:
    Алгоритм делит массив на подмассивы длины min_run и сортирует каждый из них с помощью сортировки вставками.
    Для этого используется цикл for, который проходит по массиву arr с шагом min_run.
    Внутри цикла вызывается функция insertion_sort() для каждого подмассива.
    """
    min_run = 32
    n = len(arr)
    # данный алгоритм работает в зависимости от длины массива

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(
                left=arr[start:midpoint + 1], right=arr[midpoint + 1:end + 1])
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr


def counting_sort(arr):
    """
    Этот алгоритм in-place сортирует массив, выбрал специально 2 разных подхода
    Также является одним из быстрых
    """
    size = len(arr)
    output = [0] * size

    # Максимальное значение в массиве, чтобы знать, сколько различных элементов нужно отсортировать
    max_value = max(arr) + 1

    # Создаем массив для подсчета количества вхождений каждого элемента
    count = [0] * max_value

    # Подсчитываем количество вхождений каждого элемента
    for i in range(0, size):
        count[arr[i]] += 1

    # Суммируем значения в массиве count, чтобы знать конечную позицию каждого элемента в отсортированном массиве
    for i in range(1, max_value):
        count[i] += count[i - 1]

    # Заполняем output в правильном порядке
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    # Копируем отсортированные значения обратно в исходный массив
    for i in range(0, size):
        arr[i] = output[i]


arr = random.sample(range(1, 1000), 64)

start_time = time.time()
print(tim_sort(arr))
print(f"{tim_sort.__name__} обошлся в {time.time() - start_time}")


start_time = time.time()
counting_sort(arr)
print(f"{counting_sort.__name__} обошлся в {time.time() - start_time}")



