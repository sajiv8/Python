a=[[1, 2, 8, 6], [3, 4, 9, 10], [0, 4, 5, 7], [3, 5, 4, 9]]

for i in range(len(a)):
    new=[]
    for j in a:
        new.append(j[i])
    print(''.join(new))
            


