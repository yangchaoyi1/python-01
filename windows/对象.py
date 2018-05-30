class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def info(self):
        print("学生：%s;分数：%s"%(self.__name,self.__score))
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            print("请重新输入！")
stu = Student('xiaoming',95)
print("修改前：",stu.get_score())
stu.info()
stu.set_score(10)
print("修改后：",stu.get_score())
stu.info()
