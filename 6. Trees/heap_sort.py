from heapq import heappush, heappop
from typing import Iterable


def heap_sort[T](data: Iterable[T]) -> list[T]:
    heap: list[T] = []
    for elem in data:
        heappush(heap, elem)
    result: list[T] = []
    while heap:
        result.append(heappop(heap))
    return result


if __name__ == '__main__':
    print(heap_sort([23, 8, 4, 42, 16, 15]))
    print(heap_sort('hello world'))
