"""THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS."""

from UC3MTravel.HotelManager import HotelManager
from pathlib import Path

def main():
    """Function to try and check methods and functions"""
    # MAIN PROGRAM
    hotel = HotelManager()
    """result1 = hotel.room_reservation(5555555555554444,
                                    "Izan Sanchez",
                                    236,
                                    561321141,
                                    "single",
                                    "18/03/2024",
                                    5)
    print(result1)
    jsonPath = (str(Path.home()) +
                "\G88.2024.T05"
                ".GE2\Arrival.json")
    result2 = hotel.guest_arrival(jsonPath)"""
    result3 = hotel.guest_checkout("fce482f0817853def241cfd787177aff7e94b842f0db2c2faf8cb3e77e24ad20")
    print(result3)







if __name__ == "__main__":
    main()
