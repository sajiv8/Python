word="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number=list(input().upper())
dig=int(input())
length=len(number)
letter=number[length-2]
index_word=word.index(letter)
new=int(number[length-1])+dig
if len(str(new))==2:
        number[length-1]=str(new)[1]
        number[length-2]=word[index_word+1]
else:
    number[length-1]=str(new)
    
print(''.join(number))
 
