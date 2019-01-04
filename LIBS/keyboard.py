#-----------------------------------------------------------------------------------------------------------
#   keyboard.py
#
#   Aug 01 2016     Initial
#   Aug 02 2016     Add mandatory parameter
#   Aug 06 2016     getString no longer returns CR
#-----------------------------------------------------------------------------------------------------------

import sys

Version = "keyboard.py 1.07 Aug 03 2016"
#-----------------------------------------------------------------------------------------------------------
def getInteger(prompt = "Enter an integer please : ", mandatory = False) :
    while True:
        try:
            sys.stdout.write(prompt)
            line = sys.stdin.readline()
            if mandatory == True and len(line)==1 :
                print "Enter something please..."
            else :
                if len(line)==1 :
                    x = 0
                else:
                    x = int(line)

                break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    return x
 
#-----------------------------------------------------------------------------------------------------------
def getFloat(prompt = "Enter a float number please : ", mandatory = False) :
    while True:
        try:
            sys.stdout.write(prompt)
            line = sys.stdin.readline()
            if mandatory == True and len(line)==1 :
                print "Enter something please..."
            else : 
                if len(line)==1 :
                    f = 0.0
                else:
                    f = float(line)

                break
        except ValueError:
            print("Oops!  That was no valid float.  Try again...")
    
    return f
#-----------------------------------------------------------------------------------------------------------
def getString(prompt = "Enter a string please : ", mandatory = False) :
    while True:
        sys.stdout.write(prompt)
        line = sys.stdin.readline()
        if mandatory == True and len(line)==1 :
            print "Enter something please..."
        else : 
            break
    
    return line[:-1]
