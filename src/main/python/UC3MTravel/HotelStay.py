""" Class HotelStay (GE2.2) """
import hashlib
from datetime import datetime
from datetime import timedelta
class hotelStay():
    """This class contains all the information related with the stay of the
    guest, meaning, its localizer, idCard, information about the reservation
    and also the room key that he/she needs for staying in the hotel."""
    def __init__(self, idcard, localizer, numdays, roomtype):
        """We add a disabled message for pylint since our convention of naming
        attributes is in camelCase, but we need private attributes (__)"""
        self.__alg = "SHA-256" # pylint: disable=invalid-name
        self.__type = roomtype # pylint: disable=invalid-name
        self.__idcard = idcard # pylint: disable=invalid-name
        self.__localizer = localizer # pylint: disable=invalid-name
        specificDate = datetime(2024, 1, 1)
        self.__arrival = specificDate.strftime('%Y-%m-%d') # pylint: disable=invalid-name
        justnow = datetime.utcnow()
        """self.__arrival = justnow.strftime("%Y-%m-%d")  # pylint: disable=invalid-name"""
        departure = justnow + timedelta(days= int(numdays))
        self.__departure = departure.strftime('%Y-%m-%d') # pylint:
        # disable=invalid-name

    def signature_string(self): # pylint: disable=invalid-name
        """Composes the string to be used for generating the key for the room
         """
        # Original code

        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + str(self.__arrival) + \
            ",departure:" + str(self.__departure) + "}"
    @property
    def idCard(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @idCard.setter
    def idCard(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def roomKey(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.signature_string().encode()).hexdigest()

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value
