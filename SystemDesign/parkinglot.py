import datetime
import time

class Ticket():
    def __init__(self, space):
        self.ticketNum = space
        self.datetime = datetime.datetime.now()
        
class Parkinglot():
    def __init__(self, val):
        self.space = val

    def updateSpace(self, increment: bool):
        if increment:
            self.space += 1
        else:
            self.space -= 1

    def getTicket(self):
        if self.space > 0:
            ticket = Ticket(self.space)
            self.updateSpace(False)
            return ticket
        else:
            return
    
    def getCost(self, ticket: Ticket):
        startTime = ticket.datetime
        endTime = datetime.datetime.now()
        d = (endTime - startTime)
        diff = d.total_seconds()
        cost = 0.6
        self.updateSpace(True)
        return (diff/60) * cost

lot = Parkinglot(100)
t1 = lot.getTicket()
print(f'Ticket is {t1.ticketNum}')
time.sleep(5)
#print(f'Cost is {lot.getCost(t1)}')

t2 = lot.getTicket()
print(f'Ticket is {t2.ticketNum}')
time.sleep(10)
print(f'Cost is {lot.getCost(t2)}')
print(f'Cost is {lot.getCost(t1)}')