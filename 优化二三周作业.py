#第二周课堂作业优化代码
'hello,world'.replace('l','*')


print("第一题\n")


string = 'Good'.lower() + '!'
string + string + string

print("第二题01\n")

string = 'Good'
string = string.lower() + '!'
string * 3

print("第二题02\n")

string = 'Good'.lower()
lst = [string] * 3
'!'.join(lst) + '!'

print("第二题03\n")


'Fh1qoWe92QbvC'.swapcase()

print("第三题01\n")

def switch_case(string):
    lst = []
    for x in string:
        if x.isalpha():
           if x.islower():
               x = x.upper()
           else:
               x = x.lower()
        lst.append(x)
    return ''.join(lst)
    
switch_case('Fh1qoWe92QbvC')

print("第三题02\n")


SS='FhlqoWe92QbvC'
 AA=''
 for a in SS:
      if a.isdigit():
          AA+= a

          
 print(AA)


print("第四题\n")


print(sorted(lst))


print("第五题\n")

def unique_list(lst):
    seen = set()
    seen_add = seen.add
    return [x for x in lst if x not in seen and not seen_add(x)]
    
unique_list(l)

print("第六题\n")

string = 'aasdebbcaa'
d_counter = {}
for c in set(string):
    d_counter[c] = string.count(c)
d_counter

print("第七题\n")


def str_counter(string):
    counter = {'number': 0, 'letter': 0, 'space': 0, 'others': 0}
    for c in list(string):
        if c.isdigit():
            counter['number'] += 1
        elif c.isalpha():
            counter['letter'] += 1
        elif c.isspace():
            counter['space'] += 1
        else:
            counter['others'] += 1
    return counter
print(str_counter('ue2u9n#283  x278$ 1D'))


print("第八题\n")


def remove_spaces(string):
    return ''.join([s for s in string if not s.isspace()])


print("第九题\n")


def guess_number():
    import random
    result = random.randint(0, 100)
    guess_times = 5
    while guess_times > 0:
        guess = int(input('请输入一个数： '))
        if result == guess:
            print("恭喜你猜对了")
            break
        elif result > guess:
            print("很遗憾，你猜小了")
        elif result < guess:
            print("很遗憾，你猜大了")
        guess_times -= 1

print("第十题\n")



#第二周课后作业优化代码
    
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}'.format(i, j, i*j), end='\t')
    print()


print("第一题\n")


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


print("第二题\n")


def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
for i in range(11):
    print(fib(i))


print("第三题01\n")


fib_cache = {0: 0, 1: 1}
def fibonacci(n):
    if n not in fib_cache:
        fib_cache[n] = fibonacci(n-2) + fibonacci(n-1)
    return fib_cache[n]
for i in range(11):
    print(fibonacci(i))    

print("第三题02\n")



#第三周课堂作业优化代码

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


def has_null_value(lst):
    return list(filter(None, lst)) == lst


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


def max_in_three(x, y, z):
    from functools import reduce
    return reduce(lambda x, y: x if x > y else y, (x, y, z))


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




#第三周课堂作业优化代码
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

print("第一题\n")
    
def check_existence_of_number(lst, number):
    try:
        idx = lst.index(number)
        if idx <= len(lst) // 2:
            return 'left'
        else:
            return 'right'
    except ValueError:
        return False

print("第二题\n")


def shusu(n):
    if n==1:
        return 1
    for i in range(2,n):
        if n%i==0:
            return n
    lst=[]
    for k in range(1,101):
        lst.append(k)

b=list(filter(shusu,lst))
print(b)


print("第三题\n")


import homework04


print("第四题\n")


from functools import reduce
lst1=[1,2,3,5,6,7,5,-8,-10,-77]
def samll(x,y):
     if x>y:
         return y
     else:
         return x

def ol(lst):
     abc=reduce(samll,lst)
     return abc

print(ol(lst1))


print("第五题\n")

def get_min_value(lst):
    from functools import reduce
    return reduce(lambda x, y: x if x < y else y, lst)
print("第五题02\n")


