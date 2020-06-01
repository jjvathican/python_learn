import sys
a=sys.argv[2]
f = open('e:/hello.txt', 'w')
f.write(str(a))
f.close()