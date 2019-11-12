def binSearch (arr, start, end, x):
   if end >= start:
      mid = start + (end- start)//2
      if arr[mid] == x:
          return mid+1
      elif arr[mid] > x:
          return binSearch(arr, start, mid-1, x)
      else:
          return binSearch(arr, mid+1, end, x)
   else:
      return -1


with open('rosalind_bins.txt') as f:
    n=int(f.readline())
    m=int(f.readline())
    A=list(map(int,f.readline().split()))
    K=list(map(int,f.readline().split()))
    
with open('rosalind_bins_out.txt', 'w') as f:
    for k in K:
        f.write(str(binSearch(A,0,len(A)-1,k))+' ')

