"""For now, we are using this file to record information about the functions
of GE2. Then we will store those functions in HotelManager"""
from datetime import datetime
from datetime import timedelta
import json
import hashlib
from pathlib import Path
from UC3MTravel.HotelReservation import HotelReservation
from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManagementException import hotelManagementException
from UC3MTravel.HotelStay import hotelStay


# Main
def main():
    """A main created to try and see if the function works"""
    # Define the relative path to the file
    myManager = HotelManager()
    #print("Result: " + myManager.room_reservation(4539677908016808, "Maria Sanchez", 999, 999999999, "suite", "01/01/2024", 1))
    filePath = (str(Path.home()) +
                "\G88.2024.T05"
                ".GE2\Arrival.json")
    print(myManager.guest_arrival(filePath))
    #myManager.guest_checkout("33f55582784c90b0435378800b0fbb788a6020c37577b7ae63858406d1bb2ec5")

'''
    time_now = datetime.utcnow()
    arrival_date = time_now - timedelta(2)
    time1 = arrival_date.strftime('%Y-%m-%d')
    print(time1)
    print(time_now.timestamp())'''


if __name__ == "__main__":
    main()
