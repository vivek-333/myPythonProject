num=int(input('enter the numbers : '))
temp=num
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10
if rev==temp:
    print('yes it is a palindrom and its value = {}'.format(rev))
else:
    print('no it is not a palindrom = {}'.format(rev))     