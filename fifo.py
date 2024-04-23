from abc import ABC, abstractmethod
from typing import Union
import time


class ABCFifo(ABC):
    @abstractmethod
    def push(self, value):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class FifoV1(ABCFifo):
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items is None


class FifoV2:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = self.Node(value)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

    def is_empty(self):
        return self.head is None


def test_fifo(fifo: Union[FifoV1, FifoV2]):
    print(fifo.is_empty() == True)

    start = time.time()

    for i in range(1,100):
        fifo.push(i)
    for _ in range(1,100):
        fifo.pop()

    print(f"{type(fifo)} сделал 100 операций за {time.time() - start}")


test_fifo(FifoV1())
test_fifo(FifoV2())