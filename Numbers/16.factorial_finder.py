#Factorial Finder
def factorial_loop(n):
    total=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            total*=i
        return total

def factorial_recursion(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*factorial_recursion(n-1)
print(factorial_loop(5))
print(factorial_recursion(5))
