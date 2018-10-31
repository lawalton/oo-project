class Event():
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.listOfTasks = []
        self.areTasksDone = False

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def addTask(self, new_task):
        self.listOfTasks.append(new_task)




