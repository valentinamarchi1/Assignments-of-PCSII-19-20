def insert(n,arr):
    counter=0
    for i in range(1,len(arr)):
        k=arr[i]
        x=i-1
        while x>=0 and k<arr[x]:
            arr[x+1]=arr[x]
            x-=1
            counter+=1
        arr[x+1]=k
    return counter
        
        
with open('rosalind_ins.txt') as f:
    n=int(f.readline())
    A=list(map(int,f.readline().split()))
