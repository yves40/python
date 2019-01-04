#-----------------------------------------------------------------------------------------------------------
#   Manager.py
#
#   Aug 04 2016     Initial
#   Aug 05 2016     Overload the constructor to provide the job name automatically
#-----------------------------------------------------------------------------------------------------------

from Person import Person

class Manager(Person):

    def __init__(self, name, pay):              # Redefine constructor
        Person.__init__(self, name, 'Manager', pay) # Run original with 'mgr'
        self.innerversion = 'Manager 1.07, Aug 05 2016'

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
    def getphone(self):
        return "Manager !!!!! ", self.phone
    def setphone(self, phone):
        self.phone = phone.replace(" ", "")
        