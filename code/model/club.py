class Club():
    def __init__(self, name):
        self.name = name
        self.listOfEvents = []
        self.listOfMembers = []
        self.numMembers = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getListOfEvents(self):
        return self.listOfEvents

    def setListOfEvents(self, newList):
        self.listOfEvents = newList

    def getListOfMembers(self):
        return self.listOfMembers

    def setListOfMembers(self, newList):
        self.listOfMembers = newList

    def getNumMembers(self):
        return self.numMembers

    def setNumMembers(self, numMembers):
        self.numMembers = numMembers

    def addMember(self, student):
        self.listOfMembers.append(student)
        self.numMembers += 1

    def addEvent(self, event):
        self.listOfEvents.append(event)
    




