import re
#实现一个装饰器：检查被装饰的函数所传入的参数，如果是字符串类型，且含有小写字母，则将小写字母全部转为大写字母
def time(func):
    def Wrapper(*args,**akg):
        print(type(args))
        new_args=[]
        for i in range(len(args)):
            print(type(args[i]))
            if type(args[i])==type("aa"):
                 if not args[i].isupper():
                       print(args[i])
                       new_args.append(args[i].upper())
                 else:
                      print(args[i])
                      new_args.append(args[i])
        print(new_args)
        x=func(*new_args,**akg)
        return x
    return Wrapper

@time
def addB(x,y):
    return x+y

addB("adhjasgf","SHDASFDF")


print("第一题\n")



#实现一个生成器函数：模拟数据库中的主键自增，即生成的值为主键自增的结果
def add(a):
    while 1:
        yield a

a=baaa(1)
for i in range(10):
    print(next(b))
    
b.close()


#实现一个生成器表达式：生成 50 以内的偶数，并用 for 循环打印出每个值
def add(a):
    while 1:
        if(not a%2) and a<=50:
            yield a
        a=a+1
        
b=add(0)
for i in range(26):
    print(next(b))

b.close()




