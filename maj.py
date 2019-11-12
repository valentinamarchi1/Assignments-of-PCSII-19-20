def majorityelement(lst):
    for i in lst:
        c=lst.count(i)
        if c>len(lst)/2:
            return i
    else:
        return -1

        
with open('rosalind_maj.txt') as f:
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
        lst3.append(majorityelement(lst2[x]))
    
with open('rosalind_maj_out.txt', 'w') as f:
    lst3=list(map(str,lst3))
    f.write(' '.join(lst3))
    