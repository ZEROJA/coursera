#1.写一个函数：请用列表推导式实现整数列表的立方
def triplr(lst):
    a=[x**3 for x in lst]
    return a

if __name__=='__main__':
    triplr([1,2,3,4,5])
    print(triplr([1,2,3,4,5]))



#2.写一个函数：输入参数是一个整数列表，使用reduce函数和lambda表达式实现求和
from functools import reduce
def abc(lst):
    return reduce(lambda x,y:x+y,lst)

print(abc([1,2,3,4,5]))



#3.实现一个生成器函数：读取文件时每次只返回固定的长度，此长度可由用户调用时设置
def readaa():
    f=''
    for i in range(100):
        f+=str(i)
        f+="\n"
    with open("000.txt",'w+') as ff:
        ff.write(f)
    with open("000.txt") as f:
        while 1:
            aa=f.readline()
            yield aa
a=readaa()
print("请输入需要读取的文件长度:",end="")
for i in range(int(input())):
    print(next(a),end="")


#4.写一个函数：输入参数是一个 list，判断该 list 中是否有空对象（用两种方法实现）
#方法一
def has_null_value(lst):
    flag = True
    for x in lst:
        if not bool(x):
            break
    else:
        flag = False
    return flag

#方法二
lst=[0,False,'0',0.0,()]
def space(lst):
     a=[i==False for i in lst]
     print(a)

space(lst)



#5.写一个函数，使用递归实现10 内的斐波那契数列
def fibo(n):
    if (n <= 2):
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    num = int(input("请输入你要输出的斐波那契数列的项数："))
    if num < 0:
        print("请输入一个正整数")
    else:
        print("斐波那契数列的前{}项为：".format(num))
        for i in range(1, num + 1):
            print(fibo(i), end=" ")



#6.编写密码生成器
def passwd_gen(p_len, lower_case=True, upper_case=True, number=True, special_char=True):
    import string, random
    lower_case_set = set(list(string.ascii_lowercase))
    upper_case_set = set(list(string.ascii_uppercase))
    number_set = set([x for x in range(10)])
    special_char_set = set(list('~!@#$%^&*()'))
    user_choice = set()
    if lower_case:
        user_choice = user_choice | lower_case_set
    if upper_case:
        user_choice = user_choice | upper_case_set
    if number:
        user_choice = user_choice | number_set
    if special_char:
        user_choice = user_choice | special_char_set
    passwd_lst = random.sample(user_choice, p_len)
    return ''.join(passwd_lst)



#7.使用偏应用函数实现一个函数求2和其他整数的积
from functools import partial
add=partial(lambda x,y:x*y,2)
print(add(int(input("输出一个数:"))))



#8.实现一个装饰器：计时函数从执行开始到执行完毕所花费的时间
import time
def timeit(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        print('Start')
        rs=func(*args,**kwargs)
        [i for i in range(100001)]
        print('Consume time:',time.time()-start_time)
        return rs
    return wrapper

@timeit
def add(x,y,z):
    return x+y+z

add(100,200,300)