from UC3MTravel.HotelReservation import HotelReservation
from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManagementException import HotelManagementException

import datetime

def room_reservation (credit_card, name_surname, id_Card, phone_number,
                      room_type, arrival_date, num_days):

    hotel = HotelManager()

    # PROCESS 1 (Check Inputs)

    # Credit_card
    #Check if it is the correct format
    if (credit_card.isdigit() == False) or len(credit_card) != 16:
        raise HotelManagementException("Invalid credit card format")
    # Check if the number is valid
    if hotel.validatecreditcard(credit_card) == False:
        raise HotelManagementException("Invalid credit card number")

    # name_surname
    strings = name_surname.split()
    if len(strings) < 2:
        raise HotelManagementException("Invalid name and surname")

    # id_Card
    # I don't know how to check this

    # phone_number
    if len(phone_number) != 9:
        raise HotelManagementException("Invalid phone number")

    # room_type
    if room_type not in ["single", "double", "suite"]:
        raise HotelManagementException("Invalid room type")

    # arrival_date
    if len(arrival_date) != 10:
        raise HotelManagementException("Invalid arrival date format")
    parts = arrival_date.split('/')
    if len(parts) != 3:
        raise HotelManagementException("Invalid arrival date format")
    if not all(part.isdigit() for part in parts):
        raise HotelManagementException("Invalid arrival date format")
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    if day < 1 or day > 31:
        raise HotelManagementException("Invalid day in arrival date")
    if month < 1 or month > 12:
        raise HotelManagementException("Invalid month in arrival date")
    current_year = datetime.datetime.now().year
    if year < current_year or year > 9999:
        raise HotelManagementException("Invalid year in arrival date")

    # num_days
    if num_days < 1 or num_days > 10:
        raise HotelManagementException("Invalid number of days")
