r=4
while r>=1:
    c=4
    while c>=1:
        if r==c or c==1 or r==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c-1
    print()
    r=r-1            