def baby_sqrt(s: float, delta: float=1e-10) -> float:
    if s < 0:
        raise ValueError(f'Cannot compute the square root of {s}')
    if s == 0:
        return 0.0
    x_current: float = s / 2
    while True:
        x_new: float = (x_current + s / x_current) / 2
        if abs(x_current - x_new) < delta:
            return x_new
        x_current = x_new


if __name__ == '__main__':
    n: float = 0.0
    print(f'The square root of { n } is { baby_sqrt(n, 0.1) }.')
