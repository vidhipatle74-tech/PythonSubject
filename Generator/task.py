"""
def gen_asm(a,b):
    yield(a+b)
    yield(a-b)
    yield(a*b)
print(tuple(gen_asm(10,20)))
"""

def gen(a,b):
    x=a+b
    y=a-b
    z=a*b
    v=a//b

    yield x
    yield y
    p.close()
    yield z
    yield v
p=print(next(gen(10,5)))
print(p)
print(next(gen(10,5)))


