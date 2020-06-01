t=[1,2,3]
c=0
p=0
table=[[[1,3],[2,3]],
       [[3,3],[1,3]],
       [[2,3],[3,3]]]


while(c<3):
    i=table[c][p][0]
    m=0
    try:
       while(t[m]!=i):
           m=m+1
    except:
        m=m-1

    if m==len(t):
        print ("already assigned")
        p=p+1
    else:
        txt = open("e:/time_table.txt", "w")
        txt.write("hai")
        del t[m]
        c=c+1
        p=0
        table[c][p][1]=table[c][p][1]-1




