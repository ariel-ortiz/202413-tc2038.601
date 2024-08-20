x = 5
y = 9
z = 15

print(bin(x))
print(oct(y))
print(hex(z))

s = '1010'
print(int(s, 10))
print(int(s, 2))
print(int(s, 8))
print(int(s, 16))
print(int(s, 36))

print(f'{x & y = :08b}')
print(f'{x & z = :08b}')
print(f'{x | y = :08b}')
print(f'{x | z = :08b}')
print(f'{x ^ y = :08b}')
print(f'{x ^ z = :08b}')
print(f'{x << 1 = }')
print(f'{y << 2 = }')
print(f'{x >> 1 = }')
print(f'{y >> 2 = }')
print(f'{35 << 3 = }')
print(f'{35 >> 3 = }')
