from collections import Counter
z=[]
x=int(input("Enter the number of inputs u want to give"))
for y in range(x):
    a=int(input("Enter the number"))
    z.append(a)
Counter(z)