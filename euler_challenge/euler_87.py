import functions as funcs
from time import time

primes1 = [x**2 for x in range(2, 7071) if funcs.isPrime(x)]
primes2 = [x**3 for x in range(2, 368) if funcs.isPrime(x)]
primes3 = [x**4 for x in range(2, 84) if funcs.isPrime(x)]

ctr = []

for i in primes1:
    # if i % 1000 == 0:
    #     print i
    for j in primes2:
        for k in primes3:
            num = i + j + k
            if num >= 50000000:
                break
            ctr.append(num)            #
            # else:
            #     if num not in ctr:
            #         ctr.append(num)
a = time()
len(ctr)
print time() - a
a = time()
len(set(ctr))
print time() - a
a = time()
set(ctr).__len__()
print time() - a
