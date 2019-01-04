#-----------------------------------------------------------------------------------------------------------
#   testmymodule.py
#
#   Aug 01 2016     Initial
#   Aug 02 2016     Test from import
#   Aug 03 2016     try / catch block
#   Aug 06 2016     Test the getString and add displays
#-----------------------------------------------------------------------------------------------------------

import keyboard as mk
from keyboard import getString


Version = "testmymodule.py 1.01 Aug 02 2016"

print Version
print mk.Version, "\n\n"

try : 

    # Get a number
    number = mk.getInteger()
    print "getInteger, no params : ", number
    # Get another int 
    number2 = mk.getInteger("Enter an optional number please : ")
    print "getInteger, prompt passed : ", number2
    # Get another int 
    number3 = mk.getInteger("Enter a mandatory number please : ", True)
    print "getInteger, prompt + mandatory parameter : ", number3
    
    # Get a float
    f = mk.getFloat("Enter an optional float number please : ")
    print "getFloat, prompt passed : " , f
    # Get a float
    f = mk.getFloat("Now enter a mandatory float please : ", True)
    print "getFloat, prompt + mandatory parameter : " , f
    
    # Get a String
    string = mk.getString("Get an optional string : ")
    print "The string is :", string
    string = getString("Get a mandatory string : ", True)
    print "The string is :", string
    
except (EOFError, KeyboardInterrupt):
    # Exit without error for EOF or ^C.  Print a blank line to clear after
    # any prompt.
    print "\n\nCTL-C exit..."

print "That's it"
