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


def int_log2(n: int) -> int:
    if n <= 0:
        raise ValueError(f'int_log2 not defined for {n}')
    bit_count: int = 0
    while n:
        bit_count += 1
        n >>= 1
    return bit_count - 1


def bin_with_num_bits(n: int, b: int) -> str:
    if b < 1 or n >= (1 << b) or n < -(1 << (b - 1)):
        raise ValueError(f"Can't fit {n} into {b} bits")
    if n < 0:
        n += (1 << b)
    return f'{n:0{b}b}'
