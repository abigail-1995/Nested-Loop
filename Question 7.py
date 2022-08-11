r=1
while r<=3:
    c=1
    while c<=4:
        if r==1 or c==1 or c==4 or r==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1            