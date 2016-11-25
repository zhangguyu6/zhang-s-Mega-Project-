# coding=utf-8
'''
enter a number and find all Prime Factors (if there are any) and display them.
'''
import math
def findPrime_Factorization(n):
    primelist=[]
    for i in range(1,n+1):
        if n % i==0 and isprime(i) and i not in primelist:
            primelist.append(i)
            n = n / i
            i-=1
    return primelist

def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i==0:
            return False
    return True

def findPrime_Factor():
    while True:
        s=input('enter a number and find all Prime Factors')
        if int(s)<=10000 and int(s)>=1:
            print(str(findPrime_Factorization(int(s))))
        else:
            print('try again!')
if __name__ == "__main__":
    findPrime_Factor()
