class Ticket:
    def __init__(self,cockpitClass,passengerType,price,area='Area0',card=None):
        self.cockpitClass=cockpitClass
        self.passengerType=passengerType
        self.Price=price
        self.Area=area
        self.Card=card

    def getCockpitClass(self):
        return self.cockpitClass
    def getPassengerType(self):
        return self.passengerType
    def getPrice(self):
        return self.Price
    def getArea(self):
        return self.Area
    def getCard(self):
        return self.Card
