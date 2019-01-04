#-----------------------------------------------------------------------------------------------------------
#   klass.py
#
#   Aug 07 2016     Initial
#-----------------------------------------------------------------------------------------------------------
#
#   Declare a test class
#   It holds data attributes, shared by all instances (spam)
#
class SharedData:
    spam = 42 # Generates a class data attribute

x = SharedData() # Make two instances
y = SharedData()

print x.spam, y.spam
#
#   
#
SharedData.spam = 99
print x.spam, y.spam, SharedData.spam

x.spam = 88
print x.spam, y.spam, SharedData.spam
