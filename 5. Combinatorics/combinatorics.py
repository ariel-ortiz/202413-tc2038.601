def nicely_sorted(s: list[list]) -> list[list]:

    def size_and_content(t: list) -> tuple[int, list]:
        return (len(t), t)

    return sorted(s, key=size_and_content)

def power_set(s: list) -> list[list]:
    if not s:
        return [[]]
    recursive: list[list] = power_set(s[:-1])
    return recursive + [elem + [s[-1]] for elem in recursive]

if __name__ == '__main__':
    from pprint import pprint
    print(power_set([]))
    print(power_set(['a']))
    print(power_set(['a', 'b']))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
