from math import perm
from typing import Any


def nicely_sorted(s: list[list]) -> list[list]:

    def size_and_content(t: list) -> tuple[int, list]:
        return (len(t), t)

    return sorted(s, key=size_and_content)


def power_set(s: list) -> list[list]:
    if not s:
        return [[]]
    recursive: list[list] = power_set(s[:-1])
    return recursive + [elem + [s[-1]] for elem in recursive]


def combinations(s: list, k: int) -> list[list]:
    return [t for t in power_set(s) if len(t) == k]


def insert(x: Any, s: list, i: int) -> list:
    return s[:i] + [x] + s[i:]


def insert_everywhere(x: Any, s: list) -> list[list]:
    return [insert(x, s, i) for i in range(len(s) + 1)]


def permute(s: list) -> list[list]:
    if not s:
        return [[]]
    return sum([insert_everywhere(s[0], elem)
                for elem in permute(s[1:])],
               [])


def permutations(s: list, k: int) -> list[list]:
    return sum([permute(elem) for elem in combinations(s, k)],
               [])


if __name__ == '__main__':
    from pprint import pprint
    print(power_set([]))
    print(power_set(['a']))
    print(power_set(['a', 'b']))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    pprint(nicely_sorted(combinations(['a', 'b', 'c', 'd'], 3)))
    pprint(nicely_sorted(combinations(['a', 'b', 'c', 'd'], 2)))
    pprint(nicely_sorted(combinations(['a', 'b', 'c', 'd'], 1)))
    print(insert(5, [1, 4, 2], 1))
    print(insert(5, [1, 4, 2], 3))
    pprint(insert_everywhere(8, [1, 2, 3, 4]))
    pprint(nicely_sorted(permute(['a', 'b', 'c', 'd'])))
    pprint(nicely_sorted(permutations(['a', 'b', 'c', 'd'], 2)))
