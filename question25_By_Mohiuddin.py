class Find:
    def judge(self,val):
        self.val=val
        while(1):
            if self.val in range(ord('a'),ord('z')):
               print("lower case character")
               break
            elif self.val in range(ord('A'),ord('Z')):
                print("upper case character")
                break
            elif self.val in range(ord('0'), ord('9')):
                print("number")
                break
            else:
                print("special character")
                break

char=input("enter char you want to check")
ascval=ord(char)
obj=Find()
obj.judge(ascval)