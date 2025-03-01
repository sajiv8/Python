def get_sum(number):
    sum=0
    for i in range(1,number+1):
        if number%i==0:
            sum+=i
    sum_1=0
    for j in range(1,sum+1):
        if sum%j==0:
            sum_1+=j
    return(sum_1)
        

#q=list(map(int,input().split()))
#for m in q:
m=int(input())
sup_list=[]
for n in range(1,m+1):
    final=get_sum(n)
    if final/n==2.0:
        sup_list.append(n)
print(max(sup_list))
