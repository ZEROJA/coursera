def abc(symobl):
    x=int(input("请输入一个数："))
    y=int(input("请输入二个数："))
    if(symobl=="+"):
        result=add(x,y)
    elif(symbol=="-"):
        result=sub(x,y)
    elif(symbol=="*"):
        result=mul(x,y)
    elif(symbol=="/"):
        result=div(x,y)
    print("结果：",result)
    
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
