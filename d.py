n=list(map(float,input().split()))
Maximum=max(n)
Minimum=min(n)
if len(n)!=10:
    print("Enter only 10 numbers")
else:
    if Minimum is float:
        print("Minimum =",Minimum)
    else:
        print("Minimum =",int(Minimum))
    if Maximum is float:
        print("Maximum =",Maximum)
    else:
        print("Maximum =",int(Maximum))
        
