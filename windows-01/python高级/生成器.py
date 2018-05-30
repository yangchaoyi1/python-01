def creatNum():
    a,b = 0,1
    for i in range(5):
        yield b
        a,b = b,a+b
a = creatNum()
for num in a:
    print(num)
