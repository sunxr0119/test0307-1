# -*- coding:utf-8 -*-

# def count():
#     fs = []
#     print("闭环外")
#     for i in range(1, 4):
#         def f():
#             print("闭环内")
#             return i*i
#         fs.append(f)
#     return fs

def count():
    print("闭环外")
    def f(j):
        print("闭环内")
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()

#print(f1())
print(f2())
#print(f3())