class Train:
    def __init__(self, name, fare, seats):
        self.name= name
        self.fare= fare
        self.seats= seats
    
    def getStatus(self):
        print("#############################")
        print(f"The name of Train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("#############################")
    
    def fareInfo(self):
        print(f"The price of ticket is Rs {self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print("Your ticket has been booked!!")
            self.seats= self.seats - 1
        else:
            print("Sorry no seats available")
    
    def cancelTicket(self, seatNo):
        pass


cust1 = Train("IA Express", 90, 2)
cust1.fareInfo()
cust1.getStatus()

cust1.bookTicket()
cust1.getStatus()

cust1.bookTicket()
cust1.getStatus()

cust1.bookTicket()
cust1.getStatus()