class Employee:
    langauge="PYTHON" #This is  a class attribute
    salary=1200000

harry =Employee()
harry.name="harry" #This is a instance attribute
print(harry.name,harry.salary,harry.langauge)

Ankit=Employee()
Ankit.name="Ankit kumar"
print(Ankit.name,Ankit.langauge,Ankit.salary)

#Here name is instance attribute and salary and langauge are class attribute belong to the class