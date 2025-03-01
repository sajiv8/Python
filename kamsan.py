S = input()
L1 = list(S)
for i in range(len(L1)):
    if i > 0 and L1[i] == L1[i-1]:
        break
    count = 1
    L2 = L1[i+1:]
    for j in L2:
        
        if L1[i] == j:
            count += 1
        else:
            break
    print((count,int(L1[i])),end=' ')
