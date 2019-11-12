def three_sum(i):
    n = []
    ordered = sorted(i)
    for l in range(len(i)-2):
        a = ordered[l]
        m = l+1
        s = len(i)-1
        while m < s:
            b = ordered[m]
            c = ordered[s]
            if a+b+c == 0:
                n.append(i.index(a)+1)
                n.append(i.index(b)+1)
                n.append(i.index(c)+1)
                return(sorted(n))
            elif a+b+c > 0:
                s-=1
            elif a+b+c < 0:
                m+=1
    return [-1]

with open('rosalind_3sum.txt') as f:
    r=f.readline()
    arr=list(map(int,f.readline().split()))
    print ( *three_sum(arr) )