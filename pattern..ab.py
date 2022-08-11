a=int(input("enter num"))
k=0
i=1
while i<=a:
    b=a
    while b>=i:
        print(" ",end=" ")
        b=b-1
    j=1
    k=k+1
    while j<=i:
        print(k,end=" ")
        j=j+1
    print()
    i=i+2        