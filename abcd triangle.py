word="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter=input().upper()
ind_let=word.index(letter)
count=(2*ind_let)+1
m_ind=ind_let
start=[]
for i in range(count+1):
    line=list("."*count)
    for k in range(m_ind-i,m_ind+i+1):
        line[k]=word[i]
        line[m_ind-i]=word[i]
        line[m_ind+i]=word[i]
       

    print(''.join(line))




    
    
    
