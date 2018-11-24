import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from student import *
class StudentFactory(object):

    def getStudent(self, studentType, name, year, args):
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






