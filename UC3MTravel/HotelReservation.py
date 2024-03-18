import hashlib
import json
from datetime import datetime

class HotelReservation:
    def __init__(self, IDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber, room_type,numdays):
        self.__crEDITcardnumber = creditcardNumb
        self.__idcard = IDCARD
        justnow = datetime.utcnow()
        self.__ARRIVAL = datetime.timestamp(justnow)
        self.__NAME_SURNAME = nAMeAndSURNAME
        self.__phonenumber = phonenumber
        self.__roomtype = room_type
        self.__num_days = numdays

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__idcard,
                     "name_surname": self.__NAME_SURNAME,
                     "credit_card": self.__crEDITcardnumber,
                     "phone_number:": self.__phonenumber,
                     "arrival_date": self.__ARRIVAL,
                     "num_days": self.__num_days,
                     "room_type": self.__roomtype,
                     }
        return "HotelReservation:" + json_info.__str__()
    @property
    def CREDITCARD(self):
        return self.__crEDITcardnumber
    @CREDITCARD.setter
    def CREDITCARD(self, value):
        self.__crEDITcardnumber = value

    @property
    def IDCARD(self):
        return self.__idcard
    @IDCARD.setter
    def IDCARD(self, value):
        self.__idcard = value

    @property
    def LOCALIZER(self):
        """Returns the md5 signature"""
        json_info = {"id_card": self.__idcard,
                     "name_surname": self.__NAME_SURNAME,
                     "credit_card": self.__crEDITcardnumber,
                     "phone_number:": self.__phonenumber,
                     "arrival_date": self.__ARRIVAL,
                     "num_days": self.__num_days,
                     "room_type": self.__roomtype,
                     }
        json_string = str(json_info).replace("HotelReservation:", "").replace(
            "'", '"')
        return hashlib.md5(json_string.encode()).hexdigest()

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