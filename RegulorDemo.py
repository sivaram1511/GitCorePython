n=int(input("Enter range"))
for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(1,2*i):
        print("*",end=' ')
    print()    
