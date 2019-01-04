#-----------------------------------------------------------------------------------------------------------
#   testperson.py
#
#   Aug 04 2016     Initial
#   Aug 05 2016     Reorder some code, made too much tests
#   Aug 06 2016     Use the department class
#                   Test a namedtuple to store program info in constants
#-----------------------------------------------------------------------------------------------------------

from Person import Person
from Manager import Manager
from Department import Department
from collections import namedtuple

# Named Tupple to store constants
ProgramInfo=namedtuple('Z', ['Name','Version','Author'])     # Make a generated class
proginfo=ProgramInfo('testperson.py ', '1.13, Aug 06 2016  ', 'Y.T')

print
print proginfo.Name, proginfo.Version

# Create a few persons
bob = Person('Bob Smith', pay=100000) # Test the class
sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically
nini = Person('Barbul', 'Student', 12000)
dad = Person("Dad")
# That one is a manager, used to show some inheritance and polymorphism capabilities
# Manager inherits the Person class. 
yves = Manager('Yves', 180000)


# Now test a few methods
nini.setphone("06 88 23 45 11")
bob.giveRaise(.12)
nini.giveRaise(.05)
yves.setphone("06 08 08 08 09")
# yves is a manager, so a special giveRaise method is going to be called. Look @ Manager.py
yves.giveRaise(.1)                  # This method adds a default 10% bonus
yves.giveRaise(.1, .2)              # But you can also force a different one

print
print
# Output information in various formats
print "[ BOB ] ", bob
print "[ BOB ] ", (bob.name, bob.pay)
print "[ SUE ] ", sue.name, sue.pay
print "[ BOB ] ", ("Bob's salary is now %.2f" % bob.pay)
print "[ DAD ] ", dad

print "[ NINI ] ", nini.lastName()
print "[ NINI ] ",  nini.getphone()
print "[ YVES ] ", yves
#
#   Finally, demo polymorphism
#
bob.pay = 100000
sue.pay = 100000
nini.pay = 15000
dad.pay = 100000
yves.pay = 180000 # Manager


print('\n\nAll Persons and Managers, accessed with an object print implemented by the AttrDisplay super class\n\n')

for obj in (bob, sue, nini, dad, yves):         # Process objects generically
    print(obj)                                  # Run the common __repr__

print
print
for obj in (bob, sue, nini, dad, yves):         # Process objects generically
    print "******************", obj.lastName(), " - ", obj.getphone()

print
print
development = Department(bob, sue)      # Embed objects in a composite
development.addMember(nini)
development.addMember(dad)
development.addMember(yves)
development.giveRaises(.10)             # Runs embedded objects' giveRaise
print "Now listing the development department content\n\n"
development.showAll()                   # Runs embedded objects' __repr__

