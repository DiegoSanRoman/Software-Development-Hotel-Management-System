"""THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS."""

from UC3MTravel.HotelManager import hotelManager
from pathlib import Path

def main():
    """Function to try and check methods and functions"""
    # MAIN PROGRAM
    hotel = hotelManager()
    jsonPath = (str(Path.home()) +
                "/G88.2024.T05.GE2/src/JSONfiles/JsonForFunctions/Arrival.json")
    info = (
    5555555555554444, "Robert DeNiro", 789, 987654321, "suite", "2024-01-01",
    3)
    #result = hotel.roomReservation(*info)
    #print(result)
    hotel.guestArrival(jsonPath)







if __name__ == "__main__":
    main()
