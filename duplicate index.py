nums=list(map(int,input().split()))
nums.append(-1)
new_nums=set(nums)
if len(nums)!=len(new_nums):
    count=[]
    for i in nums:
        if nums.count(i)>1:
            repeat=nums[nums.index(i)]
            count.append(nums.index(i))
            nums[nums.index(i)]="marked"
            if repeat in nums:
                count.append(nums.index(repeat))
    list(set(count)).sort()
    for j in count:
        print(j+1,end=' ')
else:
    print("None")


