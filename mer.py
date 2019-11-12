def merge(left,right):
    result=[]
    while len(left)>0 and len(right)>0:
        if left[0]<= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    while len(left)>0:
        result.append(left.pop(0))
        
    while len(right)>0:
        result.append(right.pop(0))
    
    return result


with open('rosalind_mer.txt') as f:
    n=int(f.readline())
    A=list(map(int,f.readline().split()))
    m=int(f.readline())
    B=list(map(int,f.readline().split()))

with open('rosalind_ms_out.txt', 'w') as f:
    f.write(' '.join(map(str,merge(A,B))))



