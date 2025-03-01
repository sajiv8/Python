try:
    MAT=[]      #an empty list for store matrix
    while True:
        ROW=list(map,int(input().split()))      #getting the inputs for each row
        for j in ROW:
            if j==-1:
                break
        MAT.append(ROW)
        print(MAT)
