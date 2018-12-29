class Calculate:
    r=0
    sum=0
    def find(self,val):
        self.val=val
        self.last=(self.val)%10
        self.val = int(self.val / 10)
        while(self.val!=0):
            self.r=(self.val)%10
            self.sum=self.sum+self.r
            self.val=int(self.val/10)
        self.first=self.r
    def display(self):
        print("the value of sum of first and last digits is :",self.first+self.last)
num=int(input("enter the number :\n"))
obj=Calculate()
obj.find(num)
obj.display()