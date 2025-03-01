n=input()
vow='aeiouAIEOU'
epm=''
for char in n:
    if char in vow:
        epm+=char
    else:
        epm+=' '
x=epm.split()
long=max(x,key=len)
print(n.replace(long,f"[{long}]"))

        
