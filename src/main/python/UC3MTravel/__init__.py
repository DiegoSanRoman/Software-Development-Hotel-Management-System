"""For now, we are using this file to record information about the functions
of GE2. Then we will store those functions in HotelManager"""
from pathlib import Path
from UC3MTravel.HotelManager import hotelManager


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
    info = (5555555555554444, "Barbara Sanchez", 456, 100000000, "single", "2024-01-03", 3)
    # localizer = 388170e32dc0ba9b864085b38e0e6442
    # id = 100
    #print(myManager.roomReservation(*info))
    print(myManager.guestArrival(filePath))
    '''
    single 3 2024-01-03
    2024-01-03 2024-01-01
    None
    '''

if __name__ == "__main__":
    main()
