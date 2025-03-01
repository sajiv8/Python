a=[]
b=[]
r1,c1=map(int,input().split())
#r2,c2=map(int,input().split())
for i in range(r1):
    row1=list(map(int,input().split()))
    a.append(row1)
#for i in range(r2):
    #row2=list(map(int,input().split()))
    #b.append(row2)
for i in range(len(a)):
    new=[]
    for j in a:
        new.append(j[i])
    print(new)
            


