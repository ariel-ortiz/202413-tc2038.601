# Complexity
#    Time: O(φ^N)
#    Space: O(N)
def fibo(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    previous: int = 1
    for i in range(1, 40):
        result: int = fibo(i)
        print(f'fibo({i}) = {result} {result/previous}')
        previous = result
