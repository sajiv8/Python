n=int(input())
max = 2**n
lis = []

for i  in range(max):
    x = bin(i)[2:]
    lis.append(x.zfill(n))
print(lis)

final=[]
for i in lis:
    start = str(i[0])
    for j in range(len(i)):
        if j < len(i)-1:
            start += str(int(i[j])^ int(i[j+1]))
    final.append(int(start,2))
print(final)
