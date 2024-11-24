n= int (input())
for i in range(1,n):
    for j in range(i,n):
        if n % (i+j)==0 and j>=2 and i!=j:
            print(i,end=''),print(j,end='')





