import math

c = 0
for i in range(1000):
    for j in range(1000):
        c = i**2 + j**2
        if math.sqrt(c) + i + j == 1000:
            print math.sqrt(c) * i * j
