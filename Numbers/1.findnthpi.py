# coding=utf-8
'''Gauss–Legendre algorithm is used to compute the digits of pi'''
import math
from decimal import *
getcontext().prec = 10000
def findpi(n):
    a,b,c,d=Decimal(1),Decimal(1)/Decimal(math.sqrt(Decimal(2))),Decimal(1)/Decimal(4),Decimal(1)
    def iterfindpi(time,a,b,c,d):
        if time>10:
            return ((a + b) ** 2 / (Decimal(4) * c))
        else:
            return iterfindpi(time+1,(a+b)/Decimal(2),Decimal(math.sqrt(a*b)),c-d*((a-b)/2)**2,2*d)
    return iterfindpi(0, a, b, c, d)


def how_accute_pi():
    while True:
        s=input('how many digits of pi do you want to see?')
        if int(s)<=10000 and int(s)>=1:
            print(str(findpi(int(s)))[:int(s)+2])
        else:
            print('try again!')
if __name__ == "__main__":
    how_accute_pi()
