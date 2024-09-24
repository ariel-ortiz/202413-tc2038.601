from typing import Any, Iterator, Optional


type Tree = Optional[list[Any]]


def in_order(root: Tree) -> Iterator[Any]:
    if not root:
        return
    yield from in_order(root[1])
    yield root[0]
    yield from in_order(root[2])


def pre_order(root: Tree) -> Iterator[Any]:
    if not root:
        return
    yield root[0]
    yield from pre_order(root[1])
    yield from pre_order(root[2])


if __name__ == '__main__':
    tree: Tree = [5,
                  [3,
                   [1, None, None],
                      [4, None, None]],
                  [8,
                      None,
                      [10,
                       [9, None, None],
                          None]]]
    print(list(in_order(tree)))
    print(list(pre_order(tree)))
