class Device(object):
    """The Device class. """
     
    def __init__(self, name, level, purpose= lambda : None):
        """
        @name: a String representing the name of the device
        @level: an Int representing the permissions level necessary to trigger the device
        @purpose: a function used in order to tell the device to trigger
        """
        self.name = name
        permission_level = level
        run = purpose

    def perms(self, value_in):
        """Checks that a given user may trigger a device by comparing an input to the 
        device's necessary permission level.
        @value_in: The current user's permission level
        """
        return value_in >= self.permission_level