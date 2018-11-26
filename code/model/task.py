class Task():
    def __init__(self, name):
        self.name = name
        self.assignee = None
        self.isComplete = False

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






