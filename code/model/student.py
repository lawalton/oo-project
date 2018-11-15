import abc
class Student(abc.ABC):
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.userId = 1 #implement num

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getYear(self):
        return self.year

    def setYear(self):
        self.year = year

    @abc.abstractmethod
    def getInfo(self):
        return ""

class Member(Student):
    def __init__(self, name, year):
        Student.__init__(self, name, year)
        self.isActiveMember = False
        self.numEventsAttended = 0

    def getIsActiveMember(self):
        return self.isActiveMember

    def setIsActiveMember(self, memberStatus):
        self.isActiveMember = memberStatus

    def getNumEventsAttended(self):
        return self.numEventsAttended

    def setNumEventsAttended(self, num):
        self.numEventsAttended = num

    def getInfo(self):
        member_str = self.getName() + " is a " + str(self.getYear()) + ", is "
        if self.getIsActiveMember():
            member_str += "an active member "
        else:
            member_str += "not an active member "
        num_events = self.getNumEventsAttended()
        event_str = "and has attended " + str(num_events) + " events."

        return (member_str + event_str)

class Officer(Student):
    def __init__(self, name, year):
        Student.__init__(self, name, year)
        self.position = ""
        self.numEventsHelped = 0

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getNumEventsHelped(self):
        return self.numEventsHelped

    def setNumEventsHelped(self, num):
        self.numEventsHelped = num

    def getInfo(self):
        position_str = self.getName() + " is a " + str(self.getYear()) + ", is the " + str(self.getPosition())
        event_str = " and has helped with " + str(self.getNumEventsHelped()) + " events."
        return (position_str + event_str)




