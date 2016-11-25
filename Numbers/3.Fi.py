# coding=utf-8
'''
 generate the Fibonacci sequence to  the Nth number.
'''
def Fibonacci(n):
    def iterFibonacci(a,b,times):
        if times==n:
            return a
        else:
            return iterFibonacci(b,a+b,times+1)
    return iterFibonacci(1,1,1)

def how_accute_Fi():
    while True:
        s=input('which digits of Fi do you want to see?')
        if int(s)<=10000 and int(s)>=1:
            print(str(Fibonacci(int(s))))
        else:
            print('try again!')
if __name__ == "__main__":
    how_accute_Fi()
