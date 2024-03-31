"""For now, we are using this file to record information about the functions
of GE2. Then we will store those functions in HotelManager"""
from pathlib import Path
from freezegun import freeze_time
from UC3MTravel.HotelManager import hotelManager
@freeze_time('2024-01-01')


# Main
def main():
    """A main created to try and see if the function works"""
    # Define the relative path to the file
    myManager = hotelManager()
    '''
    filePath = (str(Path.home()) +
                "\G88.2024.T05"
                ".GE2\Arrival.json")
    myManager.guestArrival(filePath)
    # ROOM KEY = 256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6
    '''


    # Tests for the development of function 3
    filePath = (str(Path.home()) + "\G88.2024.T05.GE2\src\JSONfiles\JsonForFunctions\Arrival.json")
    info = (5555555555554444, "Barbara Sanchez", 456, 123456788, "single", "2024-01-01", 1)
    # localizer = 96350e37cb66e2d6c5143ad15fa62060
    # id = 456
    print(myManager.roomReservation(*info))
    #print(myManager.guestArrival(filePath))
    #myManager.guestCheckout("1c8ffb7df9f4a520ad0353d10386b0b921c3532e16b9e4b9e2af56da4ed1d596")


if __name__ == "__main__":
    main()
