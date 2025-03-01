matrix=[]
while True :
    row=list(map(int,input().split()))
    if row[0]==-1 and len(row)==1:
        break
    else: 
        matrix.append(row)
for i in matrix:
    length=len(i)
list1=[]
list2=[] #last row
count=len(matrix)
list1.append(matrix.pop(0))
list2.append(matrix.pop(length-2))
for j in matrix:
    list1.append(j.pop(count-1))
list1.append(list2)
for j in matrix:
    list1.append(j[::-1].pop(0))

print(list1)
