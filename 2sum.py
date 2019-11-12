def tsum (lst):
    n=[]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]+lst[j]==0:
                n.append(i+1)
                n.append(j+1)
    
    n=list(map(str, n))
    
    if n!=[]:
        string=''
        for k in n[-2:]:
            string+=k
            if k == n[-2]:
                string+=' '
        return string
    else:
        return-1

with open('rosalind_2sum.txt') as f:
    n=f.readline().strip().split()
    lst=[]
    lst2=[]
    for j in f:
        j=j.strip().split()
        lst.append(j)
    for x in lst:
        x=list(map(int,x))
        lst2.append(x)
    lst3=[]
    for x in range(0, len(lst2)):
        lst3.append(tsum(lst2[x]))
    
with open('rosalind_2sum_out.txt', 'w') as f:
    lst3=map(str, lst3)
    f.write('\n'.join(lst3))