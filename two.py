import one
print("Top level in two.py")
one.func()
if __name__ == '__main__':
    print("two.py is being directly")
else:
    print("one.py has been imported suceesfully")


