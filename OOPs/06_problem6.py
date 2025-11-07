from random import randint

class Train:


    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    def book(slf,trainNo,fro,to):# Changes self to slf then no change in Functionality
        print(f"Ticket is booked in train no: {trainNo} From {fro} to {to}")
    
    def getStatus(slf,trainNo):
        print(f"The train no: {trainNo} is running on time")

    def getFare(slf,trainNo,fro,to):
        print(f"The fare for train no: {trainNo} From {fro} to {to} is {randint(100,500)}")

t=Train(12345)
t.book(12345,"Delhi","patna")
t.getStatus(12345)
t.getFare(12345,"Delhi","patna")