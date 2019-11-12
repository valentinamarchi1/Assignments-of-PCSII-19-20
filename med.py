def quickSort(arr):
    arr=list(map(int,arr))
    left=[]
    equal=[]
    right=[]
    if len(arr)>1:
        pivot=arr[0]
        for x in arr:
            if x<pivot:
                left.append(x)
            if x==pivot:
                equal.append(x)
            elif x>pivot:
                right.append(x)
        return quickSort(left)+equal+quickSort(right)
    else:
        return arr
    
def med(arr,n):
    arr=quickSort(arr)
    return arr[n-1]
    
with open('rosalind_med.txt') as f:
    m=int(f.readline())
    A=list(map(int,f.readline().split()))
    n=int(f.readline())
    
with open('rosalind_med_out.txt', 'w') as f:
    f.write(''.join(str(med(A,n))))