'''
Decorator:  it is an functions that modifies the behaviour of other functions or methods.
            they are typically used to add functionality to functions without modifing their code
            they are created using the @ symbol

'''

def greet_gen(func):
    def wrapper():
        print("hello")
        func()
        print("take care")

    return wrapper


@greet_gen
def greet():
    print("how are you")


greet()
