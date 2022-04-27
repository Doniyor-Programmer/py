# 03:14:24

import functools

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Start")
#         result = func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper
# 
# @start_end_decorator
# 
# def add5(x):
#     return x + 5

# def print_name():
#     print("Alex")

# print_name = start_end_decorator(print_name)

# result = add5(10)
# print(result)

# print(help(add5))
# print(add5.__name__)

# print_name()


# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
# 
# @repeat(num_times=3)
# 
# def greet(name):
#     print(f"Hello {name}")
#     
# greet("Alex")


# class CountCalls:
#     def __init__(self, func):
#         self.func = func
#         self.num_calls = 0
#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f"This is executed {self.num_calls} times")
#         return self.func(*args, **kwargs)
#     
# @CountCalls
# 
# def say_hello():
#     print("Hello")
#     
# say_hello()
# say_hello()
# say_hello()