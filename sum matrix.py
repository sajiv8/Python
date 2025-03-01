n=int(input())
string=list(bin(n))
new=string[2:]
value=True
for i in range(len(new)-1):
    if new[i]=new[i+1]:
        value=False
print(value)
    





