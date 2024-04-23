№1 (enen_func.py)
Первая функция (который предоставлен в описании условий тестового задания)
Плюсы: 
- интуитивно-понятный (явно можно понять, что если при делении на 2, остаток 0, то число четное)
- лаконичный
- быстрый
Минусы: 
- не такой быстрый как вторая функция


Вторая функция:
Плюсы: 
- по идее, быстрее, т.к. нам не нужно полностью сдвигать и дополнять нулями биты + не нужно обратно в десятичную систему полученные биты переводить
- лаконичный
Минусы:
- для неопытных программистов может показаться неявным

![сравнение по времени при одинаковых данных](https://github.com/ValiaIsNotProgrammer/GameLogicTestTask/tree/master/data/even_func.png)


№2
Первый класс является базовой реализацией через списки (или можно через словарь, чтобы избежать overflow и resizing'а, но слегка пожертвовать памятью)
Плюсы: 
- простой для понимания
- относительно быстрый
Минусы:
- проблемы с памятью)

Второй класс сделан через односвязный список
Плюсы:
- Приватность и явная защищенность: будеят явно нелегко обратиться к предшетствущим узлам в очереди
- Быстрота
- Небольшие расходы в памяти
Минусы:
- Не такой простой для понимания

Третий класс сделан через классичкеский deque:
Плюсы: 
- Т.к. это усоврешенствованнная версия второго класса (двухсвязнный список, к тому же, фискированного размера), то значит быстрый
- Из-за двухсвязности есть head и tail, что позволяет получить доступ к другим узлам
- Скорость
Минусы:
- Доступ по индексу (нет приватности)
- Жертвуем памятью

![сравнение по времени при одинаковых данных](https://github.com/ValiaIsNotProgrammer/GameLogicTestTask/tree/master/data/fifo.png)

№3
первый вариант TimSort - это реализация встроенных методов сортировки. Как я понмю, создатель данного алгоритма в 2000-ух тысячных разработал его специально для Python. Основан на двух других известных алгоритма сортировки: слиянием и вставкой
Плюсы: 
- так как используются алгоритмы вставки и слияния, то проблем с памятью не должно быть
- скорость выполнения при больших данных
- Сохраняет порядок одинаковых элементов (спасибо ChatGPT, сам бы не заметил)
Минусы:
- лично мне было его сложно понять с первого раза, и, как я понимаю, для понимания он сложный
- не эффективный при маленьких данных
- средний по потреблению памяти


второй варинат CountingSort - это алгоритм сортировки для целых чисел даннных ( и по моему мнения и для строк тоже подойде, т.к. перестановка указателей для контектса строк не так сильно отличается)
Плюсы:
- Быстрый
- Относительно понятный
- Антипод TimSort, т.к. работает хорошо на маленьких данных
Минусы:
- Неэффективный в памяти
- не сохраняет порядок элементов
- слаб на больших данных

![сравнение по времени при одинаковых данных. Сделал диапозон на 1000 элементов, т.к. посчитал это оптимальным](https://github.com/ValiaIsNotProgrammer/GameLogicTestTask/tree/master/data/sorted_func.png)





