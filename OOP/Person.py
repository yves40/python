#-----------------------------------------------------------------------------------------------------------
#   Person.py
#
#   Aug 04 2016     Initial
#   Aug 05 2016     More tests on overloading methods
#-----------------------------------------------------------------------------------------------------------
from AttrDisplay import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0): # Constructor takes three arguments
        self.name = name # Fill out fields when created
        self.job = job # self is the new instance object
        self.pay = float(pay)
        self.phone = "Unknown"

    def lastName(self): # Behavior methods
        return self.name.split()[-1] # self is implied subject

    def giveRaise(self, percent):
        self.pay = self.pay * (1 + percent) # Must change here only
    
    def setphone(self, phone):
        self.phone = phone
        
    def getphone(self):
        return self.phone
        
    '''
    The second most commonly used operator overloading methods in Python, after __init__: the __repr__ method
    and its __str__ twin introduced in the preceding chapter.
    These methods are run automatically every time an instance is converted to its print string. 
    Because that is what printing an object does, the net transitive effect is that
    printing an object displays whatever is returned by the object  __str__ or __repr__
    method, if the object either defines one itself or inherits one from a superclass. Doubleunderscored
    names are inherited just like any other.
    Technically, __str__ is preferred by print and str, and __repr__ is used as a fallback
    for these roles and in all other contexts. 
    def __repr__(self): # Added method
        return '[Person (__repr__):Name : %s Salary : %.2f *** Job : %s *** Phone : %s]' % (self.name, self.pay, self.job, self.phone) # String to print
        
    def __str__(self): # str is preferred to repr by the print function, so if you overload both str prevails
        return '[Person (__str__): Name : %s Salary : %.2f *** Job : %s *** Phone : %s]' % (self.name, self.pay, self.job, self.phone) # String to print
    '''
        