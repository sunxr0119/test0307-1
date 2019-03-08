# -*- coding: utf-8 -*-

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return ("done")

#for n in fib(6):
#    print(n)


f=fib(6)
#while True:
#    try:
#        n=next(f)
#        print('f:',n)
 #   except StopIteration as e:
 #       print('Generation return value:',e.value)
  #      break
#
#yanghuisanjiao
def triangles(max):
    L = [1]
    if max==1:

        yield L
    else:
        n=0
        while n<max:
            test_L=[0]+L+[0]
            L=[]
            for index,value in enumerate(test_L):
                if index<len(test_L)-1:
                    L=L+[test_L[index]+test_L[index+1]]
            n=n+1
            yield L
    return "done"

for n in triangles(6):
    print(n)
t= triangles(6)
while True:
    try:
        n=next(t)
        print('t:',n)
    except StopIteration as e:
        print('Generation return value:',e.value)
        break