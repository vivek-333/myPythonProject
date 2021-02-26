# a = 'vivek'
# for i in range(2):

#     print (a)

# fruits = ['apple','orange','banana']
# for i in fruits:
#     print(i)


# for i in range(0,4):
#     for j in range(0,3):
       
#         print(i,end=' ')
#     print(i)     

# number1=['item1','item2','item3']
# number2=[1,2,3,4,5,6,7]
# for num in number1:
#     for item in range(len(number1)):
#         print(number2[item])
# prices=[5,10,15,20,30]
# total=0
# tax=20

# for price in prices:
#     total=total+price
# print(total)
# sum=total+tax
# print(sum)


# a=10
# if a<10:
#     print ('pen2')
# elif a!=10:
#     print('pen3')
# elif a==1:
#     print('pen4')
# else:
#     print('pen5')

# def add():
#     vol = 2+3
#     print(vol)
# add()

  

# def mult(x,y):
#     vol = x*y
#     print(vol)
# mult(4,5)

# def add(x,y,z):
#     vol = x**3+x*y*z+y+z+x*y+z
#     print(vol)

# add(4,5,3)


# import math
# def mul():
#     r= int(input('enter the value :'))
#     h= int(input('enter the value :'))
#     l= int(input('enter the value :'))
#     b= int(input('enter the value :'))
#     ans= int(r+h+l+b)
#     print(ans)
# mul()    


# list1 = [1,12,34,5]
# list2 = ['a','b','r','t']
# list3 = [1,2,3,4,5,6]
# for i in list1:
#     for j in list2:
#         for k in list3:
#             print(k,end='')
        

# colors= ['red','yellow','green']
# cars = ['audi','bmw','benzs']
# for i in colors:
#     for j in cars:
#         print(i,j)

         
# profit=[30,40,50]
# user = ['vivek','satnam','avi']
# tax = [10,35,5]
# total = 0
# for i in range(len(profit)):
#     total=total+profit[i]+tax[i]
#     print(total,user[i])
#     total = 0


# profit=[]
# tax=[]

# def abc():
#     total=0
    
#     for i in range(0,2):

#         n=int(input('enter the value of profit : '))
#         profit.append(n)
#     print(profit)
#     for i in range(0,2):

#         n=int(input('enter the value of tax : '))
#         tax.append(n)
#     print(tax)
#     for j in range(len(profit)):
#         total=total+profit[j]+tax[j]
#     print(total)
        
# abc()


# a=int(input('enter the android price : '))

# i=int(input('enter the iphone price : '))
# def fun():
#     if a>i:
#         print('a is coster then i')
#     elif a==i:
#         print('a is to i')
#     elif a<i:
#         print('i is cheaper then a')
#     elif a<=i:
#         print('i is coster than a ')
# fun()

# color1 = input('enter the color name 1 : ')

# def fun():
#     color1 = input('enter the color name 1 : ')

#     if color1=='red':
#         print('roses are red')
#     elif color1=='black':
#         print('car is black')
#     else:
#         print('mention the color')
    
# fun()


# v=['white','red']
# for i in v:
#     s=i.upper()
#     print(s,end='  ')

                          

# while True:
#     username=input('enter the username : ')
#     password=input('enter the pass : ')
        
#     if username=='vivek' and password=='12345':
#         print('correct')
#         break
#     else:
#         print('error')
        

                      # return fun

# def abc():
#     a=' apple'
#     return a 
# def cd():
#     b=' banana'
#     return (b+ abc()) 
# def eat():
#     f=' orange'
#     print(cd()+ f)
# eat()        

            #    MATRIX

# matrix=[]
# a=int(input('enter the numberof rows : '))
# b=int(input('enter the number column : '))
# for i in range(a):
#     c=[]
#     print('enter {}th row'.format(i+1))
    
#     for j in range(b):
#         c.append(int(input()))
#     matrix.append(c)
# print('this is your matrix')
# for i in range(a):
#     for j in range(b):

#         print(matrix[i][j],end=' ')
    
#     print()
    

                #   fibonaci

# def fun():
#     terms=int(input('enter the no of terms : '))
#     a=0
#     b=1
#     count=0
#     if terms==0:
#         print('invalid')
#     elif terms==1:
#         print('fibonaci series upto {} term is {}'.format(terms,a))
#     else:
#         print('fibonaci series')
#         while count<terms:
            
#             print(a)
#             c=a+b
#             a=b
#             b=c
#             count=count+1
# fun()

   
                # palindrom

# num=int(input('enter the no : '))
# temp=num
# rev=0
# while num>0:
#     r=num%10
#     rev=rev*10+r
#     num=num//10

# if rev==temp:
#     print('yes it is a palindrom and its value is : {}'.format(rev))
# else:
#     print('no it is not a palindrom {}'.format(rev))

                        #    lambda fun

# var=lambda x,y:x**+y+1
# print(var(2,3))

# def fun(n):
#     return lambda a:a*n
# var=fun(3)
# print(var(4))

                    # prime no

# num=int(input('enter the no : '))
# if num>1:
#     for i in range(2,num):
#         if (num%i)==0:
#             print('not prime')
#             break
#     else:
#         print('prime')
# else:
#     print('not prime')
            
            #  sorting

# fruits=['cherry','apple','graps','banana']
# fruits.sort()
# print(fruits)

            #  revrse sorting

# fruits=['cherry','apple','graps','banana']
# fruits.sort(reverse=True)
# print(fruits)

                # for lenght

# def length_of_cars(l):
#     return len(l)
# cars=['force','BMW','vw','tesla']
# cars.sort(key=length_of_cars,reverse=True)
# print(cars)

                # square of each element in list

# list=[1,2,3,4,5,6]
# empty_list=[]
# for i in list:
#     s=i**2
#     empty_list.append(s)
# print(empty_list)

                     #    maping
    
# def square(num):
#     return num**2

# num=[1,2,3,4,5,6]
# s=list(map(square,num))
# print(s)

#                pattern printing

# a='*'
# for i in range(0,5):
    
    

#     for j in range(0,i+1):
#         print(a,end=' ')
#     print()
    
    
# n=4
# a='*'
# no_of_space=2*n-2
# for i in range(0,n):
#     for j in range(0,no_of_space):
#         print(end=' ')
#     no_of_space=no_of_space-1
#     for k in range(0,i+1):
#         print(a,end=' ')
#     print('\n')    

# num = int(input("enter the rows : "))
# for i in range(0,num+1):
#     print('* '*i)
            

# num = int(input("enter the rows : "))

# for i in range(0,num+1):
#     print('  '*(num-i)+'* '*i)
# for i in range(num,0,-1):
#     print('  '*(num-i)+'* '*i)


# matrix=[]
# a=int(input('enter the no of rows : '))
# b=int(input('enter the no of column : '))
# for i in range(a):
#     c=[]
#     print('its {}th row'.format(i+1))
    
#     for j in range(b):
#         c.append(int(input('enter the value : ')))
#     matrix.append(c)
# print("this is  the matrix")
# for i in range(a):
#     for j in range(b):
#         print(matrix[i][j],end=' ')

#     print()
# sum=0
# for i in range(a):
#     for j in range(b):
#         if j==i:
#             sum=sum+matrix[i][j]
# print('sum of diognal element: {}'.format(sum))            

# def fun():
#     a=int(input('enter the no : '))
#     b=int(input('enter the no : '))
#     c=int(input('enter the no : '))
#     if a>b and a>c:
#         print('a is greater than b and c')
#     elif b>a and b>c:
#         print('b is greater than a and c')
#     elif c>a and c>b:
#         print('c is greater than a and b')
#     else:
#         print('no are equal')
# fun()

# a=int(input())
# n=1
# numOfSpaces=2*a-2
# for i in range(0,a):
#     for j in range(0,numOfSpaces):
#         print(end=' ')
#     numOfSpaces=numOfSpaces-2
#     for k in range(0,i+1):
        
#         print(n,end=' ')
#     n=n+1
#     print()


 
            #========= factorial ==============

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return x*(factorial(x-1))
# n=int(input())

# print(factorial(n))

        ##========== comprinsive list =============

# a=2
# num=[a*i for i in range(0,5)]
# print(num)


# num={i:i*i for i in range(1,5)}
# print(num)

# a=2
# num=[i for i in range(a)]
# print(num)

                  #============= dict =================

# dict={'name':'vivek','age':23}
# for i in dict:
#     print(i,dict[i])
    
# dict={'name':'vivek','age':23}
# for i in dict:
#     print(i,dict[i])


# a={'name':'vivek','age':23}
# b=[(i,a[i]) for i in a]
# print(b)
    
# numberGames={}
# numberGames[(1,2,4)]=8
# numberGames[(4,2,1)]=10
# numberGames[(1,2)]=12
# sum=0
# for k in numberGames:
#         sum +=numberGames[k]
# print(len(numberGames)+sum)

# a={'name':'vivek','age':23}
# for key,value in a.items():
#         print(key,value)

# a={'name':'vivek','age':23}     
# for i in enumerate(a.items()):
#         print(i)

# a={1:23,2:12,3:53,4:34}
# a.popitem()
# print(a)
      
            ###================ random =================
 
# import random
# print(random.random())

                     ##======= .split() ===========

# a='my name is vivek'
# b=a.split()
# print(b)

# a='my ,name ,is vivek'
# b=a.split(',')
# print(b)

                ##============  strip ============
         
# a= '  vivek  '
# b=a.strip()
# print(b)

#=============================================================
# import random

# lower=['abcdefghijklmnopqrstuvwxyz']
# upper=[]
# a=lower[0].upper()
# upper.append(a)
# number=['1234567890']
# special=['@#$%+-*&!']
# add=lower+upper+number+special
# b=''.join(add)
# c=random.sample(b,8)
# z=''.join(c)
# print(z)

                ##============== CALCULATOR ===============

# def calculator():
#         if operator=='+':
#                 c=a+b
#                 return('addtion of {} + {} = {}'.format(a,b,c))
#         elif operator=='-':
#                 c=a-b
#                 return('addtion of {} - {} = {}'.format(a,b,c))
#         elif operator=='*':
#                 c=a*b
#                 return('multiplication of {} * {} = {}'.format(a,b,c))
#         elif operator=='/':
#                 c=a/b
#                 return('division of {} / {} = {}'.format(a,b,c))


# if __name__ == '__main__':
#         a=int(input('first value : '))
#         b=int(input('first value : '))
#         operator=input()
#         result=calculator()


# import pywhatkit as kit 
# # kit.sendwhatmsg('+919877619142','helo tont',19,3)
# kit.playonyt('hindi songs')

         #================== classes and object ==============

# class computer:
#         def __init__(self,ram,prosessor,storage):
#                 self.ram=ram
#                 self.prosessor=prosessor
#                 self.storage=storage
#         def brand(self,brand_name):
#                 print('Brand = {} \nProsessor = {} \nram = {} \nstorage = {}'.format(brand_name,self.prosessor,self.ram,self.storage))

# hp=computer(4,'i3','1tb')
# hp.brand('HP')
# dell=computer(8,'i5','512')
# dell.brand('DELL')

class student:
        def __init__(self,name,course,roll_no):
                self.name=name
                self.course=course
                self.roll_no=roll_no
        def branch(self,branch):
                print('student name = {}\ncourse = {}\nroll no = {}\nbranch = {}'.format(self.name,self.course,self.roll_no,branch))
        def skill(self,skill):
                print('skill = {}'.format(skill))        
        
student1=student('vivek','btech',1234)
student1.branch('cse')
student1.skill('python')
student2=student('akhil','btech',1534)
student2.branch('civil')
student2.skill('java')

