def func(functionName):
    print("----1----")
    def func_in():
        print("----func_in  1------")
        ret = functionName()#保存 返回来的haha
        print("----func_in-2")
        return ret#把haha返回到15行的调用
    print("---2----")
    return func_in
@func
def test():
    print("---test---")
    return "haha"

ret = test()
print(ret)