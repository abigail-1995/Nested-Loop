r=1
while r<=7:
    c=1
    while c<=7:
        if r==4 or r+c==5 or c-r==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1            