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

with open('rosalind_par3.txt') as f:
    n=int(f.readline())
    A=list(map(int,f.readline().split()))
    
with open('rosalind_par3_out.txt', 'w') as f:
    f.write(' '.join(map(str,quickSort(A))))