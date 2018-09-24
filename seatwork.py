def prt_usr():
     name = input('name: ')
     age = int(input('age:'))
     year = 2018 + 100 -age
     r = f'{name}在{year}年为100岁'
     print(r)
     return year

prt_usr()


print("第一题\n")


def get():
     num = int(input("请输入一个整数："))
     if num % 2==1:
         print("你输入的是奇数")
     else:
         print("你输入的是偶数")

get()


print("第二题\n")


lst=[0,False,'0',0.0,()]
def space(lst):
     a=[i==False for i in lst]
     print(a)

space(lst)


print("第三题方法一\n")


def space(a):
     return a==False

b=list(filter(space,lst))
print(b)


print("第三题方法二\n")


def abc(lst):
     all(lst)==True
     if all(lst):
         print('没有')
     else:
         print('有')

lst=['','a','b']
abc(lst)


print("第三题方法三\n")

lst=list(range(1,11))
def abc(lst):
     abcd=[x*x for x in lst]
     return abcd

abcd=abc(lst)
print(abcd)


print("第四题方法一\n")


lst=list(range(1,11))
def abc(x):
     return x*x

list(map(abc,lst))


print("第四题方法二\n")


from functools import reduce
lst=list(range(1,101))
def add(x,y):
     return x+y

print(reduce(add,range(1,101)))


print("第五题\n")


def abc(lst):
     abcd=[x*x*x for x in lst]
     return abcd

abcd=abc(lst)
print(abcd)


print("第六题\n")


lst=list(range(1,20))
lst1=list(range(3,19))
def back(lst,lst1):
    lst2=[x for x in lst if x in lst1]
    return list(lst2)

lst2=back(lst,lst1)
print(lst2)


print("第七题\n")


def mac(o,e,v):
     return max(o,e,v)

Maximum=mac(100,200,300)
print(Maximum)


print("第八题方法一\n")


def mac(x,y,z):
     if x>y:
         if x>z:
             print(x)
         else:
             print(z)
     elif x>z:
         if x>y:
             print(x)
         else:
             print(y)
     else:
         if y>z:
             print(y)
         else:
             print(z)
     return max

print(mac(12,616,18))


print("第八题方法二\n")
