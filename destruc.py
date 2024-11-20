class bike:
    def __init__(self,model,make,color):
        self.model=model
        self.make=make
        self.color=color

    def __del__(self):
        print(f'deleting {self.make}{self.color}')


mybike=bike("honda","2012","blue")
