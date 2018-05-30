age = input ("请输入你的年龄:")#input获取的所有数据都当做字符串类型
age_num = int (age)#整形，去除双引号之后的值
#if 如果年龄大于18
if age_num>18:
    print("已成年")
else:
    print ("未成年")