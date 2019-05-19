"""Generators Example
"""

# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(4):
    print(x)




my_gen = ( n*n for n in range(4))
for x in my_gen:
    print(x)