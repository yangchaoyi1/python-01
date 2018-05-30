"""
try:
    print("try……")
    r = 10/0
    print("result: ",r)
except Exception as e:
    print("except: ",e)
finally:
    print("finally……")
print("end")"""
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(' ',fact(-1))
