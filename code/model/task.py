from student import Student
class Task():
    def __init__(self, name, student):
        self.name = name
        self.assignee = student
        self.isComplete = False
        self.priority = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAssignee(self):
        return self.assignee

    def setAssignee(self, assignee):
        self.assignee = assignee

    def getIsComplete(self):
        return self.isComplete

    def setIsComplete(self, isComplete):
        self.isComplete = isComplete

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority






