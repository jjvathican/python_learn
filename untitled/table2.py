p=0
table=[[[1,3],[2,3]],
       [[3,3],[1,3]],
       [[1,3],[4,3]]]
txt = open("a:/time_table.txt", "w")
while(p<3):
    c = 0
    s = 0
    p = p + 1
    print(p)
    ts = [1, 2, 3, 4]
    while(c<3):
        for cnt in range(0, 1):
            if (sti < table[c][cnt][1]):
                s = cnt
                sti = table[c][cnt][1]
        m = 0
        def fun():

            while (ts[m] != st):
                m = m + 1
            else:
                s=s-1
                st = table[c][s][0]
