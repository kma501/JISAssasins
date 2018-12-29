class Find:
    def get(self,f,s,t):
        self.f=f
        self.s=s
        self.t=t
        if self.f+self.s>self.t and self.f+self.t>self.s and self.t+self.s>self.f:
            print("Triangle is possible .")
        else:
            print("Triangle is not possible .")

first=int(input("enter the length of first side of triangle :"))
second=int(input("enter the length of 2nd side of triangle :"))
third=int(input("enter the length of 3rd side of triangle :"))
obj=Find()
obj.get(first,second,third)
