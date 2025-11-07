def get_details():
    name=input("Enter your name:")
    roll=input("Enter your roll number:")
    marks=[]
    for i in range(3):
        mark=float(input(f"Enter marks of subject {i+1};"))
        marks.append(mark)
    return name,roll,marks