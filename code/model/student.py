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
        return self.getNumEventsAttended

    def setNumEventsAttended(self, num):
        self.numEventsAttended = num

    def getInfo(self):
        member_str = self.getName() + "is"
        if self.getIsActiveMember():
            member_str += "an active member"
        else:
            member_str += "not an active member"
        event_str = "and has attended with" + self.getNumEventsAttended() + "events."

        return (member_str + event_str)

class Officer(Student):
    def __init__(self, name, year):
        Student.__init__(self, name, year)
        self.position = ""
        self.numEventsHelped = 0

    def getPosition(self):
        return position

    def setPosition(self, position):
        self.position = position

    def getNumEventsHelped(self):
        return self.getNumEventsHelped

    def setNumEventsHelped(self, num):
        self.numEventsHelped = num

    def getInfo(self):
        position_str = self.getName() + "is the" + self.getPosition()
        event_str = "and has helped with" + self.getNumEventsHelped() + "events."
        return (position_str + event_str)




