'''
LAMBDA FUNCTION:
A lambda function is a small anonymous function defined with the lambda keyword.
'''
from pprint import pprint

# lambda argument: expression
x=lambda a:a+25
print(x(25))

x1=lambda a,b:a+b
print(x1(25,100))

x2=lambda a,b:a+b
print(x2(250,250))

def myfunc(n):
    return lambda a:a*n
mytriple=myfunc(3)
print(mytriple(11))
mydouble=myfunc(2)
print(mydouble(10))

#what is function?
#A function is a named block of reusable code that performs a specific task.

def outer(demo):
    def inner():
        print(demo)
    inner()
outer("hi there welcome to python")

def outer(meet):
    def inner(name):
        return f"{meet},{name} ,cherry"
    return inner()
outer("hello","cherry")
inne
demo=outer("hello")
print(demo("robert"))


