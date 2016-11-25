# coding=utf-8
'''
The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
'''
def Change_Return(cost,amount):
    moneykinds=[25,10,5,1]
    a=[]
    def change(value,kinds,lists):
        if value==0:
            a.append(lists)
        elif not kinds:
            return None
        elif kinds[0]<=value:
            change(value-kinds[0],kinds,lists+[kinds[0]])
            change(value,kinds[1:],lists)
            return None
        elif kinds[0]>value:
            return change(value,kinds[1:],lists)
    change(amount-cost, moneykinds, [])
    return a



def showchange():
    while True:
        c=input('cost')
        s=input('the amount of money given')
        if int(s)-int(c)>0:
            print(Change_Return(int(c),int(s)))
        else:
            print('try again!')
if __name__ == "__main__":
    showchange()