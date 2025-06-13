# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
# @repeat(3)
# def greet(): 
#     print("Hello!")
# greet()

# def my_function(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")
# my_function(name="Alice", age=30, city="New York")

# def demo(*args, **kwargs):
#     print("Positional:", args)
#     print("Keyword:", kwargs)

# demo(1, 2, 3, name="Alice", age=30)


# def log_function(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @log_function
# def greet(name):
#     print(f"Hello, {name}!")

# # greet("Ravi")


# def safe_division(func):
#     def wrapper(a, b):
#         if b == 0:
#             return "❌ Cannot divide by zero."
#         return func(a, b)
#     return wrapper

# @safe_division
# def divide(a, b):
#     return a / b

# print(divide(10, 2))
# print(divide(10, 0))


# def log_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function '{func.__name__}' called with arguments: {args} ")
#         return func(*args, **kwargs)
#     return wrapper
# @log_call
# def add(a,b):
#     print(a+b)
# add(2,3)

# current_user="guest"
# def admin_on(func):
#     def wrapper(*args,**kwargs):
#         if current_user!="admin":
#             print( "deny access")
#         return func(*args,**kwargs)
#     return wrapper
# @admin_on
# def local_system():
#     print("welcome ")
# local_system()


# def double_power(func):
#     def wrapper(*args, **kwargs):
#         num = func(*args, **kwargs)
#         return num * 2
#     return wrapper
# @double_power
# def multiply(num):
#     return num 

# print(multiply(5))
        


# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")        
# greet("Alice")

 

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         if  args and all(num > 0 for num in args):
#             print("positive")
#         return func(*args, **kwargs)
#     return wrapper                  
# @decorator
# def nums(*nums):
#     return nums
# print(nums(2,3,4,5))


def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def greet(name):
    print(f"Hello, {name}!")

greet("Ravi")
