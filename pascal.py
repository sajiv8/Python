n=int(input())
pas=[[1],[1,1]]
for i in range(n-2):
        out=[]
        out.append(1)
        for j in range(len(pas[-1])-1):
            s=pas[-1][j]+pas[-1][j+1]
            out.append(s)
        out.append(1)
        pas.append(out)
print(pas)

