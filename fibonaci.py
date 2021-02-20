def fun():
    terms=int(input('enter the no of terms : '))
    a=0
    b=1
    count=0
    if terms==0:
        print('invalid')
    elif terms==1:
        print('fibonaci series upto {} term is {}'.format(terms,a))
    else:
        print('fibonaci series')
        while count<terms:
            
            print(a,end=" ")
            c=a+b
            a=b
            b=c
            count=count+1
fun()
