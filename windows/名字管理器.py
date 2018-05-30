#1、打印提示
print("="*30)
print("    名字管理系统")
print("1、添加一个新的名字")
print("2、删除一个名字")
print("3、修改一个名字")
print("4、查询一个名字")
print("5、退出")
print("="*30)
names = []#定义一个空的列表用来存储名字
while True:
    #2、获取用户的选择
    num = int(input("请输入功能序号:"))
    #3、根据选择，执行相应的功能
    if num==1:#选项1
        new_name = input("请输入名字:")#输入字符串
        names.append(new_name)#增加名字
        print(names)#打印列表
    elif num==2:#选项2
        del_name = input("请输入要删除的名字:")#定义要删除的名字变量
        names.remove(del_name)#删除名字
        print(names)#打印列表
    elif num==3:#选项3
        change_name = input("请输入你要修改的名字:")#定义输入的旧名字变量
        change1_name = input("请输入修改后的名字:")#定义输入的新名字变量
        sub_name = names.index(change_name)#定义旧名字的下标
        names[sub_name] = change1_name#更改名字
        print(names)#打印列表
    elif num==4:#选项4
        find_name = input("请输入要查询的名字:")#定义要寻找的名字变量
        if find_name in names:#判断是否有此名字
            print("找到此人")#正确输出
        else:
            print("没有此人")#错误输出
    elif num==5:#选项5
        break#退出选项
    else:#输入除1-5选项之外的选项
        print("输入错误")
