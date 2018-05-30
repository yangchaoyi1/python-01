def test(number):
    print("11111")
    def test_in(number2):
        print("2222")
        print(number+number2)
    print("3333")
    return test_in

ret = test(200)

ret(10)