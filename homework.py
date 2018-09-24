def abc(lst,x):
    if x in lst:
        print("yes,",x," in lst")
        c=[x==i for i in lst]
        d=0
        for abcd in c:
            d+=1
            if abcd==True:
                break;
        y=d/len(lst)
        if y<=0.5:
            print("left")
        else:
            print("right")
    else:
        print("no")

lst=list(range(101))
abc(lst,5)


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
