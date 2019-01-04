#-----------------------------------------------------------------------------------------------------------
#   klassinheritance.py
#
#   Aug 07 2016     Initial
#-----------------------------------------------------------------------------------------------------------
class Super:
    def method(self):
        print('in Super.method') # Default behavior
    def delegate(self):
        self.action() # Expected to be defined
    def action(self):
        raise NotImplementedError('action() must be defined in your provider class!')

class Inheritor(Super): # Inherit method verbatim
    pass

class Replacer(Super): # Replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super): # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super): # Fill in a required method
    def action(self):
        print('in Provider.action')

class BadProvider(Super): pass
    
# Start here ................................................................. 
if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    #
    # Demonstrate what happens if the provider class does not have the proper method
    # The delegate method for y will call self.action(). 
    # As it's not found in the BadProvider class, Super.action() is called and an exception raised
    #
    print('\nProvider...')
    x = Provider()
    x.delegate()
    try: 
        y = BadProvider()
        y.delegate()
    except Exception, message: 
        print 'Houston, got a problem : ', message
    
    
