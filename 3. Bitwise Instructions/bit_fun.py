def is_even(n: int) -> bool:
    return (1 & n) == 0


def is_power_of_2(n: int) -> int:
    return False if n == 0 else (n & (n - 1)) == 0
