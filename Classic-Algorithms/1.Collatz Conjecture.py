#Collatz Conjecture
def collatz_conjecture(n):
    countn=0
    while n!=1:
        if n%2==0:
            n=n/2
            countn+=1
        else:
            n=n*3+1
            countn+=1
    return countn

print(collatz_conjecture(27))




