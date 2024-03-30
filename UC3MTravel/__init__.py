"""For now, we are using this file to record information about the functions
of GE2. Then we will store those functions in HotelManager"""
from datetime import datetime
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
    filePath = (str(Path.home()) +
                "\G88.2024.T05"
                ".GE2\Arrival.json")
    myManager.guest_arrival(filePath)
    # ROOM KEY = 256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6

    # temporary tests for the development of function 3

    myManager.guest_checkout("256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6")
    #myManager.guest_checkout("256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac7")
    '''
    specificDate = datetime(2024, 3, 18)
    timestamp = specificDate.timestamp()
    print(timestamp) # POSIX timestamp
    date_to_utc = datetime.utcfromtimestamp(timestamp)
    print(date_to_utc)
    time_now = datetime.utcnow()
    print(time_now)

    time1 = date_to_utc.strftime('%Y-%m-%d')
    time2 = time_now.strftime('%Y-%m-%d')
    print(time1)
    print(time2)
    '''

if __name__ == "__main__":
    main()
