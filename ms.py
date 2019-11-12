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


def merge_sort(lst):
    if len(lst)==1:
        return lst
    left=lst[:len(lst)//2]
    right=lst[len(lst)//2:]
    
    left=merge_sort(left)
    right=merge_sort(right)
   
    return merge(left,right)


with open('rosalind_ms.txt') as f:
    n=int(f.readline())
    A=list(map(int,f.readline().split()))
    
with open('rosalind_ms_out.txt', 'w') as f:
    f.write(' '.join(map(str,merge_sort(A))))