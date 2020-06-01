txt = open("e:/teacher.txt", "r")
i=0
a=[0,0,0,0,0]
while(i<5):
    a[i] = txt.readline()
    i= i+ 1
txt.close()
