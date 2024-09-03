from __future__ import annotations
from collections.abc import Iterator, Iterable
from typing import cast


class _Node[N]:

    info: N | None
    next: _Node[N]
    prev: _Node[N]

    def __init__(self, value: N | None = None) -> None:
        self.info = value
        self.next = self
        self.prev = self


class OrderedSet[T]:

    __sentinel: _Node[T]
    __count: int

    # Complexity: O(N^2), where N = len(values)
    def __init__(self, values: Iterable[T] = []) -> None:
        self.__sentinel = _Node()
        self.__count = 0
        for elem in values:
            self.add(elem)

    # Complexity:  O(1)
    def __iter__(self) -> Iterator[T]:
        current: _Node[T] = self.__sentinel.next
        while current != self.__sentinel:
            yield cast(T, current.info)
            current = current.next

    # Complexity: O(N)
    def __repr__(self) -> str:
        return f'OrderedSet({ list(self) if self else "" })'

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity: O(N)
    def __contains__(self, value: T) -> bool:
        for elem in self:
            if value == elem:
                return True
        return False

    # Complexity: O(N)
    def add(self, value: T) -> None:
        if value in self:
            return
        self.__count += 1
        new_node: _Node[T] = _Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(N)
    def discard(self, value: T) -> None:
        current: _Node[T] = self.__sentinel.next
        while current != self.__sentinel:
            if current.info == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.__count -= 1
                return
            current = current.next

    # Complexity: O(N^2 + N*M), where N = len(self) and M = len(other)
    def __and__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    # Complexity: O(N*M), where N = len(self) and M = len(other)
    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if not isinstance(other, OrderedSet):
            return False
        if len(self) != len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    # Complexity: O(N*M), where N = len(self) and M = len(other)
    def __le__(self, other: OrderedSet[T]) -> bool:
        if self is other:
            return True
        if len(self) > len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True


if __name__ == '__main__':
    a: OrderedSet[str] = OrderedSet()
    print(f'{a = }')
    print(f'{bool(a) = }')
    a.add('enero')
    a.add('febrero')
    a.add('febrero')
    a.add('marzo')
    a.add('abril')
    a.add('enero')
    print(f'{a = }')
    print(f'{len(a) = }')
    print(f'{bool(a) = }')
    for elem in a:
        print(elem)
    print(f'{"marzo" in a = }')
    print(f'{"septiembre" in a = }')
