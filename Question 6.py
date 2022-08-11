r=1
while r<=4:
    c=1
    while c<=4:
        if c==1 or c==4 or c==r:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1            