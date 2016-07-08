import functions as funcs


n = 600851475143
a = list(funcs.factors(n))
# a = [1, 3, 7]
prime_factors = [x for i, x in enumerate(a) if funcs.isPrime(a[i])]
print max(prime_factors)
