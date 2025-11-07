class Vector:
    def __init__(self,list):
        self.l=1
        

    # def __add__(self,other):
    #     result = Vector(self.x + self.x ,self.y + self.y, self.z + other.z)
    #     return result
    
    # def __add__(self,other):
    #     result=self.x * other.x +self.y * other.y + self.z * self.z
    #     return result
    
    # def __str__(self):
    #     return f"vector({self.x} ,{self.y}, {self.z})"
    
    def __len__(self):
        return 3
    

v1=Vector({1,2,3})
print(len(v1))