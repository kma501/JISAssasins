# question number 1 by Mohiuddin
class Find:
    def calculate(self,no):
        self.no=no
        string = str(self.no)
        length = len(string)
        if length==4:
            codd=0
            ceven=0
            czero=0
            while(self.no!=0):
                r=self.no%10
                val=r%2
                if r==0:
                    czero=czero+1
                else:
                    if val==0:
                        ceven=ceven+1
                    else:
                        codd=codd+1
                self.no=int(self.no/10)
            print(czero)
            print(codd)
            print(ceven)
        else:
            print("sorry the entered number is not of four digit")

val=int(input("enter the four digit number you want to check :\n"))
num=Find()
num.calculate(val)