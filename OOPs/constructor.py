class Employee:
    language = "PYTHON"  # Class attribute
    salary = 1200000

    def __init__(self,name,salary,language):   # ✅ fixed underscores and indentation(dunder method is automatically called when an object is created)
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee("harry",120000,"javascript")
harry.name = "Harry"
print(harry.name, harry.salary,harry.language)


