vowel=['a','e','i','o','u']
n=input()
x=list(n)
a=[]
temp_out = ''
i = 0
while i<len(x):
    current = x[i]
    try:
        next = x[i+1]
    except:
        next = ''
    if current in vowel:
        temp_out += current
        if next in vowel:
            temp_out += next
            i += 2
        else:
            a.append(temp_out)
            temp_out = ''
    else:
        a.append(temp_out)
        temp_out = ''
    i += 1
        
maxx = ''
for m in a:
    if len(m)>len(maxx):
        maxx = m
if len(maxx)>0:
    
    x.insert(n.index(maxx), '[')

    x.insert(n.index(maxx) + len(maxx) + 1, ']')

print(''.join(x))
            
            
