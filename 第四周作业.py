class Animal():
    name='animal'
    def call():
        pass

class Dog(Animal):
    name='dog'
    def call(a):
        print( "我叫"+a.name+"汪汪")

class Cat(Animal):
    name='cat'
    def call(a):
        print("我叫"+a.name+"喵喵")

dog=Dog()
dog.call()
cat=Cat()
cat.call()


print("第一题\n")


def fibo(n):
      if(n<=2):
          return 1
      else:
          return fibo(n-1)+fibo(n-2)

if __name__=="__main__":
     num=int(input("请输入你要输出的斐波那契数列的项数："))
     if num<0:
         print("请输入一个正整数")
     else:
         print("斐波那契数列的前{}项为：".format(num))
         for i in range(1,num+1):
             print(fibo(i),end=" ")

             
print("第二题\n")


print(list(x for x in range(1, 101) if x % 2 != 0))


print("第三题\n")



def abc(symobl):
    x=int(input("请输入一个数："))
    y=int(input("请输入二个数："))
    try:
        if(symobl=="+"):
            result=add(x,y)
        elif(symbol=="-"):
            result=sub(x,y)
        elif(symbol=="*"):
            result=mul(x,y)
        elif(symbol=="/"):
            result=div(x,y)
        print("结果：",result)
    except:
        print("no!")
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if b!=0:return x/y
    else:
        print("除数不能为零")


abc("+")


print("第四题\n")
