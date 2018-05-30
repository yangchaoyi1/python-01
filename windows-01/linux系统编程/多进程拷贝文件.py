from multiprocessing import Pool,Manager
import os

def copy_file(name,old_filename,new_filename,queue):
    "完成copy一个文件的功能"
    fr = open(old_filename+"/"+name)
    fw = open(new_filename+"/"+name,"w")

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)

def main():

    #0、获取要copy的文件夹的名字
    old_filename = input("请输入文件夹的名字：")
    #1、创建一个文件夹
    new_filename = old_filename+"-副件"
    #print(new_filename)
    os.mkdir(new_filename)

    #2、获取old文件夹中的所有的文件名字
    file_name = os.listdir(old_filename)
    print(file_name)
    #3、使用多进程的方式copy 原文件夹中的所有文件到新的文件夹中
    pool = Pool(5)
    queue = Manager().Queue()
    for name in file_name:
        pool.apply_async(copy_file,args=(name,old_filename,new_filename,queue))
    num = 0
    allNum = len(file_name)
    while num<allNum:
        queue.get()
        num +=1
        copyRate = num/allNum
        print("\rcopy的进度是：%.2f%%"%(copyRate*100),end="")



if __name__ == "__main__":
    main()