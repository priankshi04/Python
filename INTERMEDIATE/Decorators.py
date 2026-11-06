# Decorators- a function that takes a function as a paramter, wraps the fn in an inner fn that performs the job it has to do and returns that inner function
def logtime(func):# use to change the behaviour of a fn without modfying the fn itself
    def wrapper():# can use when we need to perform the same code on multiple fn
        print("before")
        val=func()
        print("after")
        return val
    return wrapper
@logtime# fn has the logtime decorator assign to it
def hello():
    print("Hello")
hello()

# Decorators- a function that takes a function as a paramter, wraps the fn in an inner fn that performs the job it has to do and returns that inner function
"""def logtime(func):# use to change the behaviour of a fn without modfying the fn itself
    def wrapper():# can use when we need to perform the same code on multiple fn
        print("before")
        val=func()
        print("after")
        return val
    return wrapper
@logtime# fn has the logtime decorator assign to it
def hello():
    print("Hello")
hello()"""
import functools
def start_end_decorators(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
       print('Start')
       result= func(*args, **kwargs)
       print('End')
       return result
    return wrapper
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr=[f"{k}={v!r}" for k , v in kwargs.items()]
        signature=",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result= func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper
@debug # stack decorator will result in first debug fn , then start_end_decorator fn and then say_hello fn
@start_end_decorators
def say_hello(name):
    greeting= f'Hello {name}'
    print(greeting)
    return greeting
say_hello('Alex')
