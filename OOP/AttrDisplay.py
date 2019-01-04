#-----------------------------------------------------------------------------------------------------------
#   AttrDisplay.py
#
#   Aug 05 2016     Initial
#-----------------------------------------------------------------------------------------------------------
class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    def __gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[ Class : %10s, Attributes :  %s ]' % (self.__class__.__name__, self.__gatherAttrs())
        
