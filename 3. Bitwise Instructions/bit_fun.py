def is_even(n: int) -> bool:
    return (1 & n) == 0


def is_power_of_2(n: int) -> int:
    return False if n == 0 else (n & (n - 1)) == 0


def twos_complement(n: int) -> int:
    return ~n + 1


def int_mul(m: int, n: int) -> int:
    negative: bool = (n < 0) ^ (m < 0)
    m = abs(m)
    n = abs(n)
    result: int = 0
    while m:
        if m & 1:
            result += n
        m >>= 1
        n <<= 1
    return -result if negative else result
