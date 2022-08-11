str=input("enter num")
r=0
while r<len(str):
    c=0
    while c<=r:
        print(str[c],end=" ")
        c=c+1
    print()
    r=r+1    