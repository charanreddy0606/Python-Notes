from oops import calc
class childimp(calc):
    num2=200

    def __init__(self):
        calc.__init__(self,2,15)
    def getcompletedata(self):
        return self.num2 + self.num + self.summation()

obj=childimp()
print(obj.getcompletedata())

