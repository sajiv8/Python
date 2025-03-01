lines=int(input())
count_line=lines*2-1
med_index=(count_line-1)//2
list1=[]
for i in range(1,lines+1):
    string=list(" "*count_line)
    for k in range(med_index-i+1,med_index+i):
        string[k]="*"
    new=''.join(string)
    list1.append(new)
    
for row in list1:
    print(row)
list1.pop()
for row in list1[::-1]:
    print(row)



        
   
