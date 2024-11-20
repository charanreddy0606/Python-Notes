class employee:
    def setnumberofworkinghours(self):
        self.setnumberofworkinghours=40

    def display_no_of_workinghours(self):
        print(self.setnumberofworkinghours)


emp=employee()
emp.setnumberofworkinghours()
print("Number of working hours of employees: ",  end=' ')
emp.display_no_of_workinghours()


class trainee(employee):
    def setnumberofworkinghours(self):
        self.setnumberofworkinghours=45

    def reset_numberofworkinghours(self):
        super().setnumberofworkinghours()
Trainee=trainee()
Trainee.setnumberofworkinghours()
print("Number of working hours of trainee employees: ",  end=' ')
Trainee.display_no_of_workinghours()
Trainee.reset_numberofworkinghours()
print("no of working hours has been reset :",end=" ")
Trainee.display_no_of_workinghours()

