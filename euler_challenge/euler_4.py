import functions as funcs


temp = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if funcs.isPalendrome(i * j):
            temp = max(temp, i * j)
