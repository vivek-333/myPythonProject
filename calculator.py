def calculator():
        if operator=='+':
                c=a+b
                return('addtion of {} + {} = {}'.format(a,b,c))
        elif operator=='-':
                c=a-b
                return('addtion of {} - {} = {}'.format(a,b,c))
        elif operator=='*':
                c=a*b
                return('multiplication of {} * {} = {}'.format(a,b,c))
        elif operator=='/':
                c=a/b
                return('division of {} / {} = {}'.format(a,b,c))
        

if __name__ == '__main__':
        while True:
                a=int(input('first value : '))
                b=int(input('first value : '))
                operator=input('what you want ( + - * / ) : ')
                result=calculator()
                
                print(result)