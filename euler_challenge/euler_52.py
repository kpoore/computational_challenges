import collections as coll

for i in range(100000, 1000000):
    one = str(i)
    two = str(2 * i)
    three = str(3 * i)
    four = str(4 * i)
    five = str(5 * i)
    six = str(6 * i)

    c1 = coll.Counter(one)
    c2 = coll.Counter(two)
    c3 = coll.Counter(three)
    c4 = coll.Counter(four)
    c5 = coll.Counter(five)
    c6 = coll.Counter(six)
    if c1 == c2 and c2 == c3 and c3 == c4 and c4 == c5 and c5 == c6:
        print i, one, two, three, four, five, six
