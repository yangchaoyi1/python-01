def w1(func):
    def inner():
        print("验证")
        func()
    return inner
@w1
def f1():
    print("f1")
@w1
def f2():
    print("f2")
#inner_func = w1(f1)
#inner_func()

#f1 = w1(f1)
#f1()
f1()
f2()