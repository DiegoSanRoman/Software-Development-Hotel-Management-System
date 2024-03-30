"""THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS."""

from UC3MTravel.HotelManager import HotelManager
from pathlib import Path

def main():
    """Function to try and check methods and functions"""
    # MAIN PROGRAM
    hotel = HotelManager()
    """result1 = hotel.room_reservation(5555555555554444, "Santiago P", 100,
                                100000000, "single",
                "01/01/2024", 1)
    print(result1)"""
    jsonPath = (str(Path.home()) +
                "\G88.2024.T05"
                ".GE2\Arrival.json")
    result2 = hotel.guest_arrival(jsonPath)
    result3 = hotel.guest_checkout("2561501b6413b67f6b8a2a8a6bf21534cca970fc4dfae839f7d1390d120d29f5")
    print(result3)







if __name__ == "__main__":
    main()
