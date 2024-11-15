# Time complexity: O(φ^N)
def fibo_recursive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)


# Time complexity: O(N)
def fibo_dp(n: int) -> int:
    if n == 0:
        return 0
    dp: list[int] = [0] * (n + 1)
    dp[1] = 1
    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]
    return dp[n]


if __name__ == '__main__':
    print(f'{fibo_recursive(0) = }')
    print(f'{fibo_recursive(1) = }')
    print(f'{fibo_recursive(5) = }')
    print(f'{fibo_recursive(9) = }')
    print(f'{fibo_recursive(40) = }')
    print(f'{fibo_dp(0) = }')
    print(f'{fibo_dp(1) = }')
    print(f'{fibo_dp(5) = }')
    print(f'{fibo_dp(9) = }')
    print(f'{fibo_dp(40) = }')
    print(f'{fibo_dp(1000) = }')
