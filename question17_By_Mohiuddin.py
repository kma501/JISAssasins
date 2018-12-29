class Prime:
    def check(self, p):
        print("Prime numbers are\n")
        for self.x in p:
            self.flag = 0
            for self.i in range(2, self.x):
                if (self.x % self.i == 0):
                    break
                else:

                    print(self.x)
                    break


li = []
n = int(input("Enter how many number you want to insert"))
print("Enter the numbers")
i = 0
while (i < n):
    li.append(int(input()))
    i = i + 1
mohi= Prime()
mohi.check(li)