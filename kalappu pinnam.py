a,b=map(int,input().split('/'))
a_f=[]
b_f=[]
c_f=[]
for i in range(1,a+1):
    if a%i==0:
        a_f.append(i)
for k in range(1,b+1):
    if b%k==0:
        b_f.append(k)
for j in a_f:
    if j in b_f:
        c_f.append(j)
maximum_cf=max(c_f)
if a//maximum_cf<b//maximum_cf:
    print(str(a//maximum_cf)+"/"+str((b//maximum_cf)))
else:
    print(str((a//maximum_cf)//(b//maximum_cf))+"|"+str((a//maximum_cf)%(b//maximum_cf))+"/"+str(b//maximum_cf))
