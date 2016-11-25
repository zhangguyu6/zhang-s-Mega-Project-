# coding=utf-8
'''
enter a number and find all Prime Factors (if there are any) and display them.
'''
import math
class bankaccount:

    def __init__(self,total,monthrate):
        self.total=total
        self.rate=monthrate

    def monthly_payments(self,month):
        indextotal=self.total*(1.0+self.rate)**month
        indexpay=((1.0+self.rate)**month-1)/self.rate
        return indextotal/indexpay

    def paytime(self,value):
        index=self.total/value
        return math.log(1/(1.0-index*self.rate),(1.0+self.rate))


a=bankaccount(1000,0.01)#set month interest rate and amount of fixed term mortgage
print(a.monthly_payments(12))# how much it need pay  at fixed term
print(a.paytime(88))# how long it will take the user to pay back the loan at fixed month pay