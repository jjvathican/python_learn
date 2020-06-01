
p=0
table=[[[1,3],[2,3]],
       [[3,3],[1,3]],
       [[1,3],[4,3]]]
txt = open("a:/time_table.txt", "w")
while(p<3):
 c=0
 s=len(table[c])
 p=p+1
 print(p)
 ts = [1, 2, 3, 4]
 while(1):


   try:
    st = table[c][s][0]
    while(ts[m]!=st):
        m=m+1
   except:
      s=s-1

   else:

        temp=table[c][s][1]=table[c][s][1]-1
        txt.write(str(p)+" <- "+str(c+1)+" <- "+str(st)+" <- "+str(temp)+"\n")
        del ts[m]
        sti = 0
        c = c + 1
        if(c>2):
            break
        for cnt in range(0, 1):
            if (sti < table[c][cnt][1]):
                s = cnt
                sti = table[c][cnt][1]

txt.close()




