class Reverse:
    def find(self):

        msg=input("enter the sentence you want to reverse.\n")
        words=msg.split(" ")
        newmsg=list(words)
        words.reverse()
        print(' '.join(words))

obj=Reverse()
obj.find()