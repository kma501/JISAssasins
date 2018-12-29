class Find:
    def __init__(self):
        self.count = 0
    def calculate(self,p):
        self.p=p
        while(1):
            import random
            self.cnum = random.randint(100000, 999999)
            if self.cnum != self.p:
                self.count = self.count + 1
            else:
                print("count= ",self.count)
                break
val=int(input("give the four digit number'\n"))
obj=Find()
obj.calculate(val)