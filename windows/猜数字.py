#!/usr/bin/python3
#-*-coding:UTF-8-*-
#1、选择一个随机数
import random
num = random.randint(1,100)
guess = 0#猜了多少次
while True:
    #2、获取用户的输入
    num_input = int(input("请输入1-100的数字："))
    guess += 1
    #3、判断用户的输入
    if 0>num_input or num_input>100:
        print("请重新输入")
    else:
        if num_input == num:
            print("猜对了，总共猜了%d次"%guess)
            break
        elif num_input > num:
            print("数字大了")
        elif num_input < num:
            print("数字小了")
        else:
            print("系统出错")