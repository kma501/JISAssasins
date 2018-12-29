#bonus question by Mohiuddin
'''
val=int(input("give the four digit number'\n"))
import random
cnum=random.randint(1000,9999)
print("computer random digit: ",cnum)
c=0
b=0
string=str(cnum)
value=str(val)
for i in range(len(string)):
    if value[i]==string[i]:
        c=c+1
    else:
        b=b+1
print(c,b)'''

#another approach
class Find:
    import random
    cnum = random.randint(1000, 9999)
    print("computer random digit: ", cnum)
    def __init__(self):
        self.c = 0
        self.b = 0
    def calculate(self,p):
        self.p=p
        string = str(self.cnum)
        value = str(self.p)
        for i in range(len(string)):
            if value[i] == string[i]:
                self.c = self.c + 1
            else:
                self.b = self.b + 1
        print("cow value: ",self.c," bull value : ", self.b)
val=int(input("give the four digit number'\n"))
obj=Find()
obj.calculate(val)