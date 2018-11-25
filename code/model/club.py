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

    def findMember(self, name):
        for member in self.getListOfMembers():
            if member.getName() == name:
                return member

        return "No member with the name" + name + "found."

    def findEvent(self, name):
        for event in self.getListOfEvents():
            if event.getName() == name:
                return event

        return "No event with the name" + name + "found."

    def updateEvent(self, name, edited_event):
        i = 0
        for event in self.listOfEvents:
            if event.getName() == name:
                self.listOfEvents[i] = edited_event
                return True

            i += 1
        # unable to update event
        return False

    def updateMember(self, edited_member):
        i = 0
        name = edited_member.getName()
        for member in self.listOfMembers:
            if member.getName() == name:
                self.listOfMembers[i] = edited_member
                return True

            i += 1
        # unable to update member
        return False
    




