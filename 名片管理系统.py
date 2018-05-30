def print_menu():
    # 1、打印提示
    print("=" * 30)
    print("     名片管理系统")
    print("1、添加一个新的名片")
    print("2、删除一个名片")
    print("3、修改一个名片")
    print("4、查询一个名片")
    print("5、查询所有名片")
    print("6、退出")
    print("=" * 30)
print_menu()#函数打印菜单
#2、获取用户的输入
card_infors = []
while True:
    num = int(input("请输入功能序号:"))
    #3、根据用户的输入执行相应的功能
    if num==1:
        new_name = input("请输入你的名字:")
        new_qq = input("请输入你的QQ:")
        new_wechat = input("请输入你的微信:")
        new_addr = input("请输入你的地址:")
        #定义一个字典，用来存储名片
        new_infor = {}
        new_infor['name'] = new_name
        new_infor['qq'] = new_qq
        new_infor['wechat'] = new_wechat
        new_infor['addr'] = new_addr
        #将一个字典添加到列表里
        card_infors.append(new_infor)
        #print(card_infors)#for test
    elif num==2:
        del_name = input("请输入要删除的名片的名字:")
        del_1 = 0
        for temp in card_infors:
            if del_name== temp['name']:
                card_infors.remove(temp)
                del_1 = 1
                break
                #print(card_infors)#for test
                # 判断是否找到了
        if  del_1 == 0:
            print("查无此人")
    elif num==3:
        change_name = input("请输入要更改的名片的名字:")
        change1_name = input("请输入更改后的名字:")
        change_qq = input("请输入更改后的QQ:")
        change_wechat = input("请输入更改后的微信:")
        change_addr = input("请输入更改后的地址:")
        change_1 = 0
        for temp in card_infors:
            if change_name == temp['name']:
                sub_name = card_infors.index(temp)
                change_infor={}
                change_infor['name'] = change1_name
                change_infor['qq'] = change_qq
                change_infor['wechat'] = change_wechat
                change_infor['addr'] = change_addr
                card_infors[sub_name]=change_infor
                change_1 = 1
                #print(card_infors)#for test
                break
    elif num==4:
        find_name = input("请输入要查找的姓名:")
        find_flag = 0#默认没有找到
        print("姓名\tQQ\t微信\t地址")
        for temp in card_infors:
            if find_name== temp['name']:
                print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['wechat'],temp['addr']))
                find_flag=1#表示找到了
                break
        #判断是否找到了
        if find_flag==0:#else:
            print("查无此人")
    elif num==5:
        print("姓名\tQQ\t微信\t地址")
        for temp in card_infors:
            print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['wechat'],temp['addr']))
    elif num==6:
        break
    else:
        print("输入错误")
    print("")