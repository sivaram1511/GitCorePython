n=int(input("Enter range of pattern"))
for i in range(1,n+1):
    print(" "*(i-1),end='')
    for j in range(1,n+2-i):
        print(j,end='')
    print()    
    
