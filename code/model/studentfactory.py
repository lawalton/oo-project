import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from student import *
class StudentFactory(object):
    """
    Creates different types of students
    """

    def getStudent(self, studentType, name, year, args):
        """
        Creates a type of Student based on the type.

        :param str studentType: type of student
        :param str name: student name
        :param str year: student's academic year
        :param list args: list of additional arguments required to create the student
        :return: the student
        :rtype: Member or Officer
        """
        # studentType is either "member" or "officer"
        # args is the list of arguments for that type of student
        if studentType.lower() == "member":
            student = Member(name, year)
            # args[0] is number of events attended
            student.setNumEventsAttended(args[0])
            return student

        elif studentType.lower() == "officer":
            student = Officer(name, year)
            # args[0] is number of events helped, args[1] is position
            student.setNumEventsHelped(args[0])
            student.setPosition(args[1])
            return student
        else:
            return None






