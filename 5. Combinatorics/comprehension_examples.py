# [ expression
#      for var1 in ...
#      for var2 in ...
#      ...
#      if condition1
#      if condition2
#      ...
# ]
#

# List comprehension
print([2 ** x for x in range(6)])

# List comprehension
print([c.upper() for c in 'Hello World' if c not in ' o'])

# Set comprehension
print({c.upper() for c in 'Hello World' if c not in ' o'})

# List comprehension
# Pythagorean Triples
from pprint import pprint
pprint([(a, b, c) for a in range(100)
                  for b in range(100)
                  for c in range(100)
                  if a <= b <= c and a ** 2 + b ** 2 == c ** 2])

# Dictionary comprehension
pprint({x: 2 ** x for x in range(6)})

# Generator comprehension
print((2 ** x for x in range(6)))

g = (x ** 2 for x in range(1, 50_000_000))
for elem in g:
    print(elem)
    if elem % 666 == 0:
        break
