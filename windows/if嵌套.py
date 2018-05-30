"""
if xxx:
    print(xxxxx)
    if xxx:
        xxxxx
"""
'''
ticket = 1#1表示有车票  0表示没有车票
knife = 20#cm
if ticket==1:
    print("通过了车票的检测，进站")

    #判断刀的长度是否合法
    if knife<=10:
        print("通过了安检，进入候车厅")
        print("开心……")
    else:
        print("安检没有通过，等待公安处理")

else:
    print("你没有买票!")
'''
"""
sex = input("请输入你的性别：")
if sex=="男":
    color = input("你白吗？")
    money = int(input("请输入你的财产:"))
    bea = input("你美吗？")
    if color=="白" and money>=100000 and bea=="美":
        print("白富美……")
    else:
        print("矮矬穷……")
else:
    color1 = input("你高吗？")
    money1 = int(input("请输入你的财产:"))
    bea1 = input("你帅吗？")
    if color1=="高" and money1>=100000 and bea1=="帅":
        print("高富帅……")
    else:
        print("矮矬穷……")"""
""""""
#while嵌套
i = 1
while i<=5:
    j = 1
    while j<=5:
        print("*",end="")
        j+=1#c语言中让j加上1的方式：j++;   ++j;   j+=1;  j=j+1
    print("")
    i+=1

