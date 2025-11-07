class Employee:
    langauge="PYTHON" #This is  a class attribute
    salary=1200000

    def getinfo(self):
        print(f"the langauge is {self.langauge}.the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry =Employee()
# harry.langauge="javascript" #This is a instance attribute
harry.greet()
harry.getinfo()
#Employee.getinfo(harry)

