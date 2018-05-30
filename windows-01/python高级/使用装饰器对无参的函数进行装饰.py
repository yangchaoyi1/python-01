"""
def func(function_name):
    def func_in():
        print("func--2")
        function_name()
    return func_in()
@func
def foo():
    print("test-a=%d,b=%d")
foo()
"""
def time_fun(func):
    def wrapped_func(*args,**kwargs):
        print("func_")
        func(*args,**kwargs)
    return wrapped_func
@time_fun
def foo(a,b):
    print("I am foo--a=%d,b=%d"%(a,b))

foo(11,22)