
class Test(object):
    def __init__(self):
        self.__num = 100
    def set_num(self,new_num):
        print("set")
        self.__num = new_num
    def get_num(self):
        print("get")
        return self.__num
    num = property(get_num,set_num)
t = Test()
#print(t.__num)
#t.__num = 200

print(t.get_num())
t.set_num(50)
print(t.get_num())

print("-"*50)
t.num = 200
print(t.num)