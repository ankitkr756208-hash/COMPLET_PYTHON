from random import randint

class Train:


    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,trainNo,fro,to):
        print(f"Ticket is booked in train no: {trainNo} From {fro} to {to}")
    
    def getStatus(self,trainNo):
        print(f"The train no: {trainNo} is running on time")

    def getFare(self,trainNo,fro,to):
        print(f"The fare for train no: {trainNo} From {fro} to {to} is {randint(100,500)}")

t=Train(12345)
t.book(12345,"Delhi","patna")
t.getStatus(12345)
t.getFare(12345,"Delhi","patna")