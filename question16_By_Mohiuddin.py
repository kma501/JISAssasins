class Find:
    def get(self,val):
        self.val=val
        self.val=self.val+1
        print(self.val,"-->",chr(self.val))
        self.val=self.val-2
        print(self.val, "-->", chr(self.val))
give=input("give character you want :")
print(give, "-->", ord(give))
obj=Find()
obj.get(ord(give))