def paixu(li):
    n = 0
    while n < len(li):
        for i in range(len(li)):
            for two_index in range(i):
                 if li[two_index+1] < li[two_index]:
                    li[two_index+1],li[two_index]=li[two_index],li[two_index+1]
        n += 1
    print(li)
li = [5,-4,6,7,11,1,2]
paixu(li)