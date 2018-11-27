class Club():
    """
    Defines a club
    """
    def __init__(self, name):
        """
        Constructor.

        :param str name: Name of the club
        """
        self.name = name
        self.listOfEvents = []
        self.listOfMembers = []
        self.numMembers = 0

    def getName(self):
        """
        Returns the name of the club

        :return: name of the club
        :rtype: str
        """
        return self.name

    def setName(self, name):
        """
        Sets the name of the club.

        :param str name: name of the club
        """
        self.name = name

    def getListOfEvents(self):
        """
        Returns the list of club events

        :return: list of club events
        :rtype: list[Event]
        """
        return self.listOfEvents

    def setListOfEvents(self, newList):
        """
        Sets the list of club events

        :param list[Event] newList: list of club events
        """
        self.listOfEvents = newList

    def getListOfMembers(self):
        """
        Returns the list of club members

        :return: list of club members
        :rtype: list[Student]
        """
        return self.listOfMembers

    def setListOfMembers(self, newList):
        """
        Sets the list of club members

        :param list[Student] newList: list of club members
        """
        self.listOfMembers = newList

    def getNumMembers(self):
        """
        Returns the number of club members

        :return: number of club members
        :rtype: int
        """
        return self.numMembers

    def setNumMembers(self, numMembers):
        """
        Sets the number of club members

        :param int numMembers: number of club members
        """
        self.numMembers = numMembers

    def addMember(self, student):
        """
        Add a new member to the club

        :param Student student: the new member
        """
        self.listOfMembers.append(student)
        self.numMembers += 1

    def addEvent(self, event):
        """
        Add a new event to the club

        :param Event event: the new event
        """
        self.listOfEvents.append(event)

    def findMember(self, name):
        """
        Find a club member by name

        :param str name: the name of the member
        :return: the club member
        :rtype: Student
        """
        for member in self.getListOfMembers():
            if member.getName() == name:
                return member

        return None

    def findEvent(self, name):
        """
        Find a club event by name

        :param str name: the name of the event
        :return: the club event
        :rtype: Event
        """
        for event in self.getListOfEvents():
            if event.getName() == name:
                return event

        return None

    def updateEvent(self, name, edited_event):
        """
        Update a club event

        :param str name: the name of the event
        :param Event edited_event: the updated event
        """
        i = 0
        for event in self.listOfEvents:
            if event.getName() == name:
                self.listOfEvents[i] = edited_event
                return True

            i += 1
        # unable to update event
        return False

    def updateMember(self, edited_member):
        """
        Update a club member

        :param Student edited_member: the updated member
        """
        i = 0
        name = edited_member.getName()
        for member in self.listOfMembers:
            if member.getName() == name:
                self.listOfMembers[i] = edited_member
                return True

            i += 1
        # unable to update member
        return False
    




