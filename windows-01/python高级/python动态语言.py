'''class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

laowang = Person("laowang",100)
print(laowang.name)
print(laowang.age)
laowang.addr = "benjing"
print(laowang.addr)

Person.num = 200
print(laowang.num)'''
class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge
    def eat(self):
        print("%seat……"%self.name)
def run(self):
    print("%srunning……"%self.name)
p1 = Person("p1",10)
p1.eat()
p1.run = run
p1.run()#虽然p1对象中run属性已经指向了20行的函数，但是这句不正确
        #因为run属性指向