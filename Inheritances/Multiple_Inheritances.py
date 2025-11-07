class Employee:
    company ="ITC"
    name="Default name"
    salary=100000
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder:
    langauge="python"
    def printLangauge(self):
        print(f"Out of all the langauge here is your langauge: {self.langauge}")

class Programmer(Employee,Coder):
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.langauge} langauge")

a=Employee()
b=Programmer()

# print(a.company,b.company)
b.show()
b.printLangauge()
b.showLanguage()