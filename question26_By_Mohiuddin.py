bs = int(input("enter basic salary.\n"))
if bs >= 5000:
    hr = (15 / 100) * bs
    da = (150 / 100) * bs

else:
    hr = (10 / 100) * bs
    da = (110 / 100) * bs

g = bs + hr + da

print("basic salary", bs, "hra is", hr, "da is", da, "gross salary is", g)