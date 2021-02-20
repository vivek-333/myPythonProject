
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
# for i in range(1,num+1):
#     print('* '*i)
            


num = int(input("enter the rows : "))
for i in range(0,num+1):
    print('  '*(num-i)+'* '*i)
for i in range(num,0,-1):
    print('  '*(num-i)+'* '*i)
