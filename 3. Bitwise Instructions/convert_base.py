def int_to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n:
        remainder = n % base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(remainder - 10 + ord('A')))
        n //= base
    return ''.join(digits[::-1])

# Examples
print(int_to_base(255, 2))  # Output: '11111111'
print(int_to_base(255, 8))  # Output: '377'
print(int_to_base(255, 16)) # Output: 'FF'
print(int_to_base(666, 36)) # Output: 'II'
