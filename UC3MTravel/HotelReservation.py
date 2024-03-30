"""This module contains akk the info related with the Reservation creation
class"""


import hashlib
from datetime import datetime


class hotelReservation:
    """This class will store information about the guest that reserves the
    room and his/her arrival date and number of days. To not have to deal
    with pylint errors in private attributes, we just disable them."""
    def __init__(self, id_card, credit_card, name_surname,
                 phonenumber,room_type, arrival_date, numdays):
        self.__crEDITcardnumber = credit_card # pylint: disable=invalid-name
        self.__idcard = id_card # pylint: disable=invalid-name
        self.__ARRIVAL = arrival_date # pylint: disable=invalid-name
        self.__NAME_SURNAME = name_surname # pylint: disable=invalid-name
        self.__phonenumber = phonenumber # pylint: disable=invalid-name
        self.__roomtype = room_type # pylint: disable=invalid-name
        self.__num_days = numdays # pylint: disable=invalid-name

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        # VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        jsonInfo = {"id_card": self.__idcard,
                     "name_surname": self.__NAME_SURNAME,
                     "credit_card": self.__crEDITcardnumber,
                     "phone_number:": self.__phonenumber,
                     "arrival_date": self.__ARRIVAL,
                     "num_days": self.__num_days,
                     "room_type": self.__roomtype,
                     }
        return "HotelReservation:" + jsonInfo.__str__()

    @property
    def creditCard(self):
        """To return the creditcard value"""
        return self.__crEDITcardnumber

    @creditCard.setter
    def creditCard(self, value):
        self.__crEDITcardnumber = value

    @property
    def idCard(self):
        """Yo return the id value"""
        return self.__idcard

    @idCard.setter
    def idCard(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Returns the md5 signature"""
        jsonInfo = {"id_card": self.__idcard,
                     "name_surname": self.__NAME_SURNAME,
                     "credit_card": self.__crEDITcardnumber,
                     "phone_number:": self.__phonenumber,
                     "arrival_date": self.__ARRIVAL,
                     "num_days": self.__num_days,
                     "room_type": self.__roomtype,
                     }
        jsonString = str(jsonInfo).replace("HotelReservation:", "").replace(
            "'", '"')
        return hashlib.md5(jsonString.encode()).hexdigest()


"""
from datetime import datetime

# Assume timestamp is the timestamp you got
timestamp = datetime.timestamp(datetime.utcnow())

# Convert timestamp to datetime
dt_object = datetime.fromtimestamp(timestamp)

# Format datetime as a string
date_string = dt_object.strftime("%d/%m/%Y")

print(timestamp)
print(dt_object)
print(date_string)
"""
