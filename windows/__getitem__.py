class Fib(object):
    def __getitem__(self, item):
        a,b = 1,1
        for x in range(item):
            a,b=b,a+b
        return a
fib = Fib()
fib[4]