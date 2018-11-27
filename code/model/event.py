class Event():
    """
    Defines a club event
    """
    def __init__(self, name, date):
        """
        Constructor

        :param str name: the event name
        :param str date: the event date
        """
        self.name = name
        self.date = date
        self.listOfTasks = []

    def getName(self):
        """
        Returns the name of the event

        :return: name of the event
        :rtype: str
        """
        return self.name

    def setName(self, name):
        """
        Sets the name of the event

        :param str name: name of the event
        """
        self.name = name

    def getDate(self):
        """
        Returns the date of the club

        :return: date of the club
        :rtype: str
        """
        return self.date

    def setDate(self, date):
        """
        Sets the date of the event.

        :param str date: date of the event
        """
        self.date = date

    def addTask(self, new_task):
        """
        Add a new task to the event

        :param Task new_task: the new task for the event
        """
        self.listOfTasks.append(new_task)

    def getTasks(self):
        """
        Returns the list of tasks for the event

        :return: list of tasks for the event
        :rtype: list[Task]
        """
        return self.listOfTasks

    def findTask(self, name):
        """
        Find a task for the event by name

        :param str name: the name of the task
        :return: the task
        :rtype: Task
        """
        for task in self.getTasks():
            if task.getName() == name:
                return task

        return None




