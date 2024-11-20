'''
Exception:

'''
try:
    l = 10
    b = 0
    print(l / b)
except Exception:
    print("division by zero is invalid kindly change ur input")


try:
    l = 10
    b = 0
    print(l / b)
except ZeroDivisionError:
    print("division by zero is invalid kindly change ur input")

try:
    l = 45
    print(l / w)
except Exception:
    print("variable is not defined")

try:
    l = 45
    print(l / w)
except NameError:
    print("variable is not defined")


try:
    w=0
    print(l/w)
except Exception:
    print("i am an error")
except Exception:
    print("variable has been used before defining it")
except ZeroDivisionError:
    print("division by 0 is invalid")


try:
    w=0
    print(l/w)

except Exception:
    print("variable has been used before defining it")
except ZeroDivisionError:
    print("division by 0 is invalid")
except Exception:
    print("i am an error")


try:
    #a=int(input("enter a value 0-9"))
    result=25/0   # zero division error
    dict1={'lion':10}
    value = dict1['lion']  # key Error
except ValueError as ve:
    print(f"value error: {ve}")
except ZeroDivisionError as zd:
    print((f"ZeroDivisionError :{zd}"))
except KeyError as ke:
    print(f"KeyError :{ke}")
else:
    print(f"result :{result}")
finally:
    print("Execution is completed")

