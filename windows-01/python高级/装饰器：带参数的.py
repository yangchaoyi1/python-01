def func_arg(arg):
    def func(functionName):
        def func_in():
            print("记录日志--arg=%s"%arg)
            if arg=="haha":
                functionName()
                functionName()
            else:
                functionName()
        return func_in
    return func
#1、先执行func_arg("haha")函数，这个函数return的结果是func这个函数的引用
@func_arg("haha")
def test():
    print("---test---")
#带有参数的装饰器，能够起到在运行时有不同的功能
test()