def func(functionName):
    def func_in(*args,**kwargs):
        ret = functionName(*args,**kwargs)
        return ret
    return func_in
@func
def test():
    print("---test---")
    return "haha"
@func
def test2():
    print("test2")
@func
def test3(a):
    print(" a=%d"%a)
ret = test()
print(ret)

test2()
test3(11)