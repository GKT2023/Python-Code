class Train:

    def __init__(self,name,train,date,source,destination,noOfSeats):
        self.name = name
        self.noOfSeats= noOfSeats
        self.train = train
        self.destination=destination
        self.date = date
        self.source = source

    def bookTicket(self):
        print(f"hello {self.name}, your ticket is booked for {self.date} from {self.source} to {self.destination} and train no is: {self.train}")

    def getStatus(self):
        print(f"no of seats are {self.noOfSeats} in {self.train} are confirmed for your journey at {self.date}")


    def getFare(self):
        print(f"your fare is {self.noOfSeats * 2000}")

t = Train("Garima","Rajdhani express","15/11/2023","mathura","pune",3)
t.bookTicket()
t.getStatus()
t.getFare()
