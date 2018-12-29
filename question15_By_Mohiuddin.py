class Power:
    def check(self,a,b,c):
        print("the number after evaluation is",(a**(b+c)))
mohi=Power()
x=int(input("Enter a number "))
m=int(input("Enter a number "))
p=int(input("Enter a number "))
mohi.check(x,m,p)