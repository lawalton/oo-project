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

    def getTasks(self):
        return self.listOfTasks
    
    def getInfo(self):
        str = self.getName() + " is on " + self.getDate() + "."
        str += " The tasks required for it are:\n"
        for task in self.listOfTasks:
            str += task.getName() + "\n"

        return str

    def findTask(self, name):
        for task in self.getTasks():
            if task.getName() == name:
                return task

        return "No task with the name" + name + "found."




