import abc
class Student(abc.ABC):
    """
    Defines a student in a club. 
    Abstract class.
    """
    def __init__(self, name, year):
        """
        Constructor
        """
        self.name = name
        self.year = year

    def getName(self):
        """
        Returns the name of the student

        :return: name of the student
        :rtype: str
        """
        return self.name

    def setName(self, name):
        """
        Sets the name of the student.

        :param str name: name of the student
        """
        self.name = name

    def getYear(self):
        """
        Returns the academic year of the student

        :return: academic year of the student
        :rtype: str
        """
        return self.year

    def setYear(self, year):
        """
        Sets the academic year of the student

        :param str year: academic year of the student 
        """
        self.year = year

    @abc.abstractmethod
    def getInfo(self):
        """
        Returns a string with info about the student.
        Abstract method. 

        :return: info about student
        :rtype: str
        """
        return ""

    @abc.abstractmethod
    def eventAttended(self):
        """
        Records the student attending an event. 
        Abstract method.
        """
        return ""

    @abc.abstractmethod
    def getEventString(self):
        """
        Returns a string about the student attending or helping with an event. 
        Abstract method

        :return: how the student interacted with the event: attended or helped
        :rtype: str
        """
        return ""

    @abc.abstractmethod
    def addEvent(self, event):
        """
        Add event to the student's list of events.
        Abstract method.

        :param Event event: the event that the student attended or helped with
        """
        return None

    @abc.abstractmethod
    def getEvents(self):
        """
        Get list of the events the student has attended or helped with.
        Abstract method.

        :return: list of events the student has attended or helped with.
        :rtype: list[Event]
        """
        return None

class Member(Student):
    def __init__(self, name, year):
        Student.__init__(self, name, year)
        self.isActiveMember = False
        self.numEventsAttended = 0
        self.eventsAttended = []

    def getIsActiveMember(self):
        """
        Get the member's active member status
        
        :return: the member's active member status
        :rtype: bool
        """
        return self.isActiveMember

    def setIsActiveMember(self, memberStatus):
        """
        Set the member's active member status.

        :param bool memberStatus: the member's new active member status
        """
        self.isActiveMember = memberStatus

    def getNumEventsAttended(self):
        """
        Get the number of events the member has attended.
        
        :return: the number of events the member has attended.
        :rtype: int
        """
        return self.numEventsAttended

    def setNumEventsAttended(self, num):
        """
        Set the number of events the member has attended.

        :param int num: number of events the member has attended.
        """
        self.numEventsAttended = num

    def getEvents(self):
        """
        Get list of the events the student has attended.

        :return: list of events the student has attended.
        :rtype: list[Event]
        """
        return self.eventsAttended

    def addEvent(self, event):
        """
        Add event to the student's list of attended events

        :param Event event: the event that the student attended
        """
        self.eventsAttended.append(event)

    def eventAttended(self):
        """
        Records the member attending an event. 
        """
        self.numEventsAttended += 1

    def getEventString(self):
        """
        Returns a string about the student attending with an event. 

        :return: how the student interacted with the event: attended
        :rtype: str
        """
        return "attended"

    def getInfo(self):
        """
        Returns a string with info about the member.

        :return: info about student
        :rtype: str
        """
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
        self.eventsHelped = []

    def getPosition(self):
        """
        Get the officer's position.

        :return: the officer's position
        :rtype: str
        """
        return self.position

    def setPosition(self, position):
        """
        Set the officer's position.

        :param str position: the officer's position
        """
        self.position = position

    def getNumEventsHelped(self):
        """
        Get the number of events the member has helped with.
        
        :return: the number of events the member has helped with.
        :rtype: int
        """
        return self.numEventsHelped

    def setNumEventsHelped(self, num):
        """
        Set the number of events the member has helped with.

        :param int num: number of events the member has helped with.
        """
        self.numEventsHelped = num

    def getEvents(self):
        """
        Get list of the events the student has helped with.

        :return: list of events the student has helped with.
        :rtype: list[Event]
        """
        return self.eventsHelped

    def addEvent(self, event):
        """
        Add event to the student's list of events that they helped with

        :param Event event: the event that the student helped with
        """
        self.eventsHelped.append(event)

    def eventAttended(self):
        """
        Records the officer helping with an event. 
        Abstract method.
        """
        self.numEventsHelped += 1

    def getEventString(self):
        """
        Returns a string about the student helping with an event. 

        :return: how the student interacted with the event: helped
        :rtype: str
        """
        return "helped"

    def getInfo(self):
        """
        Returns a string with info about the officer.

        :return: info about student
        :rtype: str
        """
        position_str = self.getName() + " is a " + str(self.getYear()) + ", is the " + str(self.getPosition())
        event_str = " and has helped with " + str(self.getNumEventsHelped()) + " events."
        return (position_str + event_str)




