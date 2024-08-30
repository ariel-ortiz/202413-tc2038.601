from collections.abc import Iterator

x = 'hello'
x_it = iter(x)
try:
    while True:
        print(next(x_it))
except StopIteration:
    ...

print()

for elem in 'hello':
    print(elem)


class Pow2Iterator:

    current: int

    def __init__(self):
        self.current = 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current > 1000:
            raise StopIteration()
        result: int = self.current
        self.current *= 2
        return result

    def rewind(self) -> None:
        self.current = 1

print()

p2it = Pow2Iterator()
try:
    while True:
        print(next(p2it))
except StopIteration:
    ...


def generator_example() -> Iterator[int]:
    x: int = 5
    yield x
    x += 1
    yield x
    x *= 2
    yield x

print()

for elem in generator_example():
    print(elem)

def pow2_generator():
    current: int = 1
    while current < 1000:
        yield current
        current *= 2

print()

for elem in pow2_generator():
    print(elem)
