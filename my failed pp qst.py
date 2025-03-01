lis=list(map(int,input().split()))
n=int(input())
pairs=[]
for i in lis:
    ind=lis.index(i)
    lis.remove(i)
    for j in lis:
        pairs.append([i,j])
    lis.insert(ind,i)

dup=[]
for i in pairs:
    if i not in dup:
        dup.append(i)
print(dup)
print(n*len(dup))
