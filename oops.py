class calc:

    num=100
    def getData(self):
        print("iam now executing as method class")
    def __init__(self,a,b):
        self.firstnumber=a
        self.secondnumber=b
        print("i am called automatically when object is created")
    def summation(self):
        return self.firstnumber + self.secondnumber + calc.num
obj = calc(20,20)
obj.getData()
print(obj.num)
print(obj.summation())
