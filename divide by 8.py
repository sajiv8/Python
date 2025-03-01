n=int(input())
if len(str(n))>=2 and len(str(n))<=100:
    if n%8==0:
        print("Yes")
    else:
        new=[]
        new_other=[]
        for i in str(n):
            new.append(i)
        for i in range(len(new)):
            x=new.pop(i)
            y=''.join(new)
            if int(y)%8==0:
                new_other.append(y)
            new.insert(i,x)
        if len(new_other)!=0:
            print("Yes   m="+str(max(new_other)))
        else:
            print("NO")
    
