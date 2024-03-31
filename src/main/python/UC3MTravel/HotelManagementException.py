"""File needed for raising exceptions in other classes and functions"""
class hotelManagementException(Exception):
    """This will contain the info necessary to represent an error message in
    screen"""
    def __init__(self, message):
        """We need to disable the action of pylint over message since our
        attribute is private (needs__) but pylint needs it to be in
        camelCase"""
        self.__message = message # pylint: disable=invalid-name
        super().__init__(self.message)

    @property
    def message(self):
        """Property for the message attribute"""
        return self.__message

    @message.setter
    def message(self,value):
        """Setter for assigning the correspondent value"""
        self.__message = value
