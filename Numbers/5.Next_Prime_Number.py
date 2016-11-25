# coding=utf-8
'''
 find prime numbers until the user chooses to stop asking for the next one.
'''
def findPrime():
    Primelist=[]
    i=2
    while True:
        if isprime(i,Primelist):
            Primelist.append(i)
            i+=1
            yield Primelist
        else:
            i+=1

def isprime(n,plist):
    for i in plist:
        if n % i==0:
            return False
    return True

def showfindPrime():
    c=findPrime()
    while True:
        s=input('do you want to see next primelist?Y/N')
        if s.lower()=='y':
            print(next(c))
        elif s.lower()=='n':
            quit()
        else:
            print('try again!')
if __name__ == "__main__":
    showfindPrime()