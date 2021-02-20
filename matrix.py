matrix=[]
a=int(input('enter the numberof rows : '))
b=int(input('enter the number column : '))
for i in range(a):
    c=[]
    print('enter {}th row'.format(i+1))
    
    
    for j in range(b):
        c.append(int(input()))
    matrix.append(c)
print('this is your matrix')
for i in range(a):
    for j in range(b):

        print(matrix[i][j],end=' ')
    
    print()
    
       ##sum of diolnal element

sum=0
for i in range(a):
    for j in range(b):
        if j==i:
            sum=sum+matrix[i][j]
print('sum of diognal element: {}'.format(sum))            

