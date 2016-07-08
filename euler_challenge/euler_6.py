a = [x**2 for x in range(1, 101)]
b = [x for x in range(1, 101)]

print sum(b)**2 - sum(a)
