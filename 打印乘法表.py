i = 1#竖着的行
while i<=9:
    j = 1#纵着的行
    while j<=i:
        print("%d*%d=%d\t"%(j,i,i*j),end="")
        j+=1
    print("")
    i+=1