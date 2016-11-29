#Reverse a String
def Reverse(s):
    re=[]
    for i in range(len(s)):
        re.append(s[len(s)-i-1])
    return ''.join(re)


print(Reverse('123'))

