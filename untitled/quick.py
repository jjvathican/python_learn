st = [10, 34, 23, 11, 45, 27, 38,75,43]


def partition(beg, piv, end):
    while (beg < end):
        while (st[beg] > st[piv]):
            beg = beg + 1
        while (st[end] < st[piv]):
            end = end - 1
        tem = st[beg]
        st[beg] = st[end]
        st[end] = tem
    return piv


def repeater(beg, end):
    piv = partition(beg, end, end)
    if (end-beg >=0):
        repeater(beg, piv-1)
        repeater(piv+1, end)

repeater(0,len(st)-1)
for i in range(0, len(st)):
    print(st[i])
