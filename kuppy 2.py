n=int(input())
nums=[]
mods=[]
for i in range(2,n):
    nums.append(i)
for j in nums:
    mods.append(n%j)
if mods.count(0)==0:
    print("prime")
else:
    print("Not")
        
    
    
