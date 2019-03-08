# -*- coding:utf-8 -*-
#lianxi234
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    huafen=s.split('.')
    print(huafen)

    def chr2num(s):
        return DIGITS[s]

    def xiaoshu(s):
        return reduce(lambda x,y:x/10+y,list(map(chr2num,s))[::-1])/10
    def zhengshu(s):
        return reduce(lambda x,y:x*10+y,map(chr2num,s))

    print(xiaoshu(huafen[1]), "_____", zhengshu(huafen[0]))
    return xiaoshu(huafen[1])+zhengshu(huafen[0])

print("str2float('123.456')= ", str2float('123.456'))