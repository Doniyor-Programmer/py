# 03:35:33

# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()

# for i in g:
#     print(i)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# print(sum(g))

# print(sorted(g))

# 03:39:42

# def countdown(num):
#     print("Starting")
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(4)

# value = next(cd)
# print(value)

# print(next(cd))
# print(next(cd))
# print(next(cd))


# import sys

# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1

# print(sum(firstn(10)))
# print(sum(firstn_generator(10)))
# print(sys.getsizeof(firstn(10)))
# print(sys.getsizeof(firstn_generator(10)))


# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b

# fib = fibonacci(30)
# for i in fib:
#     print(i)


# import sys
# mygenerator = (i for i in range(10) if i % 2 == 0)
# print(sys.getsizeof(mygenerator))

# mylist = [i for i in range(10) if i % 2 == 0]
# print(sys.getsizeof(mylist))
# for i in mygenerator:
#     print(i)