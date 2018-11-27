class Task():
    """
    Defines a task for a club event.
    """
    def __init__(self, name):
        self.name = name
        self.assignee = None
        self.isComplete = False

    def getName(self):
        """
        Returns the name of the task

        :return: name of the task
        :rtype: str
        """
        return self.name

    def setName(self, name):
        """
        Sets the name of the task.

        :param str name: name of the task
        """
        self.name = name

    def getAssignee(self):
        """
        Gets the assignee of the task.

        :return: the student assigned to the task
        :rtype: Student
        """
        return self.assignee

    def setAssignee(self, assignee):
        """
        Sets the assignee of the task.

        :param Student assignee: the student assigned to the task
        """
        self.assignee = assignee

    def getIsComplete(self):
        """
        Gets the completion status of the task.

        :return: the completion status of the task
        :rtype: bool
        """
        return self.isComplete

    def setIsComplete(self, isComplete):
        """
        Sets the completion status of the task.

        :param bool isComplete: completion status of the task.
        """
        self.isComplete = isComplete






