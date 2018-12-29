class String:
    def length(self,s):
        print("The length of the string is",len(s))
    def rev(self,s):
        print("The reverse of the string is",s[::-1])
    def con(self,s,s2):
        print("The string after concatenation is",s," ",s2)
    def cop(self,s):
        self.st=s
        print("The string is copied ",self.st)
    def comp(self,s,s2):
        if s==s2:
            print("The string is equal")
        else:
            print("The string is not equal")
mohi=String()
n=int(input("Enter 1 to fine the length, 2 to reverse, 3 to concatenate, 4 to copy, 5 to compare string "))
if(n==1):
    s7=input("Enter a string")
    mohi.length(s7)
elif n==2:
    s1=input("Enter a string")
    mohi.rev(s1)
elif n==3:
    s2=input("Enter a string")
    s3=input("Enter another string")
    mohi.con(s2,s3)
elif n==4:
    s4=input("Enter a string")
    mohi.cop(s4)
elif n==5:
    s5=input("Enter a string")
    s6=input("Enter another string to compare")
    mohi.comp(s5,s6)
