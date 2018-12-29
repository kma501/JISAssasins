n=int(input("Enter number of inputs:"))
arr=[]
brr=[]
i=0
j=0
while(n>0):
    a=int(input())
    arr.append(a)
    n-=1
print(arr)
arr.sort()
print(arr)