#Fizz Buzz
def Fizz_Buzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%5==0:
            print('Buzz')
        elif i%3==0:
            print('Fizz')
        else:
            print(i)

Fizz_Buzz(15)