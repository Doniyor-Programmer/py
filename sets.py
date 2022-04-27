# myset = set([1, 2, 3])
# print(myset)

# myset = set('Hello')
# print(myset)

# myset = {}
# print(type(myset))

# myset = set()
# print(type(myset))

# myset = set()
# myset.add(1)
# myset.add(2)
# myset.add(3)
# myset.remove(3)
# myset.discard(4)
# myset.clear()
# # myset.pop()

# for i in myset:
#     print(i)

# if 1 in myset:
#     print("yes")

# print(myset)


# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds.union(evens)
# print(u)

# i = odds.intersection(evens)
# i = odds.intersection(primes)
# i = evens.intersection(primes)
# print(i)


# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# diff = setA.difference(setB)
# diff = setB.difference(setA)
# diff = setB.symmetric_difference(setA)
# diff = setA.symmetric_difference(setB)
# print(diff)

# setA.update(setB)
# setA.intersection_update(setB)
# setA.difference_update(setB)
# setA.symmetric_difference_update(setB)
# print(setA)


# setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# setC = {7, 8}

# print(setB.issubset(setA))
# print(setA.issubset(setB))
# print(setB.issuperset(setA))
# print(setA.issuperset(setB))
# print(setA.isdisjoint(setC))

# 00:56:20

# setA = {1, 2, 3, 4, 5, 6}
# setB = setA
# setB = set(setA)
# setB = setA.copy()
# setB.add(7)
# print(setB)
# print(setA)

a = frozenset([1, 2, 3 ,4])
print(a)