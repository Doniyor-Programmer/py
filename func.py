# 04:53:26

# def print_name(name):
#     print(name)
# print_name("Alex")

# def foo(a, b, c):
    # print(a, b, c)
# foo(1, 2, 3)
# foo(c=1, b=2, a=3)
# foo(1, b=2, c=3)

# def foo(a, b, c, d=4):
#     print(a, b, c, d)
# foo(1, 2, 3, 7)

# def foo(a, b, *args, **kwargs):
#     print(a, b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key, kwargs[key])
# foo(1, 2, 3, 4, 5, six=6, seven=7)

# def foo(a, b, *, c, d):
#     print(a, b, c, d)
# foo(1, 2, c=3, d=4)

# def foo(*args, c, d):
#     print(c, d)
# foo(1, 2, c=3, d=4)

# def foo(*args, last):
#     for arg in args:
#         print(arg)
#     print(last)
# foo(1, 2, 3, last=100)

# def foo(a, b, c):
#     print(a, b, c)
# mylist = [0, 1, 2]
# mydict = {"a": 1, "b": 2, "c": 3}
# foo(*mylist)
# foo(**mydict)

# def foo():
#     x = number
#     print(f"number inside function: {x}")
# number = 0
# foo()

# def foo():
#     global number
#     x = number
#     number = 3
#     print(f"number inside function: {x}")
# number = 0
# foo()
# print(number)

# def foo(x):
#     x = 5
# var = 10
# foo(var)
# print(var)

# def foo(a_list):
#     a_list += [200, 300, 400]
#     a_list.append(4)
#     a_list[0] = -100
# mylist = [1, 2, 3]
# foo(mylist)
# print(mylist)

# numbers = (1, 2, 3, 4, 5, 6)
# beginning, *middle, secondlast, last = numbers
# print(beginning)
# print(middle)
# print(secondlast)
# print(last)

# mytuple = (1, 2, 3)
# mylist = [4, 5, 6]
# myset = {7, 8, 9}
# newlist = [*mytuple, *mylist, *myset]
# print(newlist)

# dict_a = {"a": 1, "b": 2}
# dict_b = {"c": 3, "d": 4}
# mydict = {**dict_a, **dict_b}
# print(mydict)