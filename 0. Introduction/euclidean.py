def gcd(a: int, b: int) -> int:
    if a == b == 0:
        raise ValueError('Values of the two inputs cannot be zero.')
    while b != 0:
        a, b = b, a % b
    return abs(a)
