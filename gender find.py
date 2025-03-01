name=input()
Letter=[]
for i in name:
    Letter.append(i)
length=len(set(Letter))
if length%2==1:
    if "b" in Letter:
        b_index=Letter.index("b")
        new_letter=Letter[b_index:]
    else:
        print("cannot identify")
        exit()
    for i in new_letter:
        if i=="b":
            pass
        index_b=new_letter.index("b")
        if i=="o":
            pass
        index_o=new_letter.index("o")
        if i=="y":
            pass
        index_y=new_letter.index("y")
    if index_b<index_o and index_o<index_y:
        print("He is a boy!")
    else:
        print("Cannot identify")
else:
    if "g" in Letter:
        g_index=Letter.index("g")
        new_letter=Letter[g_index:]
    else:
        print("cannot identify")
        exit()
        
        
    for i in new_letter:
        if i=="g":
            pass
        index_g=new_letter.index("g")
        if i=="i":
            pass
        index_i=new_letter.index("i")
        if i=="r":
            pass
        index_r=new_letter.index("r")
        if i=="l":
            pass
        index_l=new_letter.index("l")
        
    if index_g<index_i and index_i<index_r and index_r<index_l:
        print("He is a girl!")
    else:
        print("Cannot identify")

    

    

