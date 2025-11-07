class Employee:
    salary =234
    increament =20
    @property
    def salaryAfterIncreament(self):
        return (self.salary + self.salary * (self.increament/100))
    

    @increament.setter
    def increament(self,salary):
        self.increament=((salary/self.salary) -1)*100


e=Employee()
print(e.salaryAfterIncreament)
e.increament =10