def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a #it wll give you whatever a is starting , retun a
        temp = a  #0   1    1
        a = b  # 1      1    2
        b = temp + b  #1   2   3

for x in fib(5):
    print(x)
print('------------------')
#with list
def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

for x in fib2(5):
    print(x)