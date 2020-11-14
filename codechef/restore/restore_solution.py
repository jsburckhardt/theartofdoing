from array import *
b=array('i',[])
T=int(input(""))
for i in range(T):
    del b[0:]
    N=int(input(""))
    for j in range(1):
            nums = (int(x) for x in input("").split())
            for num in nums:
                b.append(num)
    for j in range(N-1,-1,-1):
        n=b[j]
        if(b[j] == j+1):
            b[j]=N-j+1
        else:
            b[j]=b[n-1]
    for j in range(N-1):
        print(b[j] ,end=" ")
    print(b[N-1])