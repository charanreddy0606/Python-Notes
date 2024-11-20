class myclass:
    def __init__(self,name):
        self.name=name
        print(f"{self.name} is  created")
    def some_func(self):
        print(f"method called on {self.name}")
    def __del__(self):
        print(f"{self.name} is destroyed")

obj1=myclass("object1")

obj1.some_func()
