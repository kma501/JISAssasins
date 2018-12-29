class Find:
    def get(self,val):
        self.val=val
        for i in range(1,11):
            print(self.val,"*",i,"=",(self.val*i))
value=int(input("give character you want :"))
obj=Find()
obj.get(value)