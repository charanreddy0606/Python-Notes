'''
built-in finction
print()
len()
type()
sum()

userdefined function
def demo():
    print ("hello world")

1.lambda function
2.recursive function
3.high order function
4.genarator function
5.decorators function
* function with no arguments and no return value
* function with argument but no return value
* function with no arugument but a return value
* function with arguments and a return value
* function with defult arguments
'''

## user defind function#
'''function with no arugument and no return valu'''
def demo():
    print("hello world")
demo()
def demo():
    print("vamshi")
demo()

'''function with arugument but no return value'''
def demo(age):
    print (f"vijay is {age}")
demo(25)

def demo(age):
    print (f"vamshi krishna is {age}")
demo(20)

'''function with no argu but return value '''
def sal():
    return 1000
newsal=sal()
print(newsal)

def sal():
    return 80000
newsal=sal()
print(newsal)

'''function with argument and return value'''
def add(a,b):
    return a+b
result=add(5,7)
print(result)

def add(a,b):
    return a+b
result=add(20,5)
print(result)

'''function with variable length arguments'''
#*args and **kwargs
def compute(length,width):
    area=length*width
    print(area)
compute(20,30)

length=200
width=400
def compute(lenth,width):
    area=lenth*width
    print(area)
compute(200,400)

'''finction with default aruguments'''
def demo(name="vijay"):
    print(f"hello{name}")
demo("vinay")

def demo(name="vamshi"):
    print(f"hello{name}")
demo("vamshi")

