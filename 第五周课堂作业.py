#使用偏应用函数实现一个函数求2和其他整数的积
from functools import partial
add=partial(lambda x,y:x*y,2)
print(add(int(input("Can you print a number:"))))


print("第一题\n")

#将柯里化的例子用偏应用函数 partial 实现
def add(x,y,z):
    return x+y+z

addA=partial(add,x=1,y=2,z=3)
addA()


print("第二题\n")


#实现一个装饰器：计时函数从执行开始到执行完毕所花费的时间
import time
def timeit(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        print('Start')
        rs=func(*args,**kwargs)
        print('Consume time:',time.time()-start_time)
        return rs
    return wrapper

@timeit
def add(x,y,z):
    return x+y+z

add(100,200,300)


print("第三题\n")


#实现一个装饰器：检查除法函数传入的参数，避免除法函数抛 ZeroDivisionError 异常
def add(w):
    def addA(a,b):
        if b!=0:
            addB=a(a,b)
            return addB
        else:
            print("ZeroDivisionError!!!")
    return addA

@add
def ab(a,b):
    return a/b
print(ab(100,0))


print("第四题\n")


#实现一个装饰器：使被装饰的函数在每次执行完毕后打印’Done’和当前时间（精确到秒）
import datetime
def timeat(a):
    def add(*args,**kwargs):
        ab=a(*args,**kwargs)
        print(datetime.datetime.now())
        return ab
    return add

@timeat
def ab(a,b,c):
    return a*b*c
print(ab(100,200,300))


print("第五题\n")
