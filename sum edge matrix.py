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
count=len(matrix)
list1.append(matrix.pop(0))
list1.append(matrix.pop(count-2))
for j in matrix:
    list1.append([j[0]])
    list1.append([j[length-1]])
sumo=0
for k in list1:
    sumo+=sum(k)
#print(list1)
print(sumo)
#for j in matrix:
   # for k in range(count):
        
