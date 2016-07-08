import fibonacci as fib

f = 0
i = 1
eve = 0
while f < 4000000:
    i += 1
    a = fib.fibonacci_rec(i)
    if a % 2 == 0:
        eve += a
    f = a

print eve
