li = []
n = int(input("Enter how many number you want to insert"))
print("Enter the numbers")
i = 0

while (i < n):
    li.append(int(input()))
    i = i + 1

print("The maximum is", max(li))
print("The minimum is", min(li))