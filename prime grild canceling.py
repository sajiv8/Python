n=int(input())
numbers=[]
new=[]
for i in range(1,n+1):
    numbers.append(i)
print(numbers)
for j in numbers:
    new.append(j)
    numbers.remove(j)
    for k in numbers:
        if k%j==0:
            numbers.remove(k)
final=numbers.extend(new)
print(final)

    
