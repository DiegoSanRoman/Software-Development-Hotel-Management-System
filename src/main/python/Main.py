"""THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS."""

from UC3MTravel.HotelManager import hotelManager


def main():
    """Function to try and check methods and functions"""
    # MAIN PROGRAM
    hotel = hotelManager()
    result1 = hotel.roomReservation(5555555555554444, "Santiago P", 100,
                                100000000, "single",
                "2024-01-01", 1)
    print(result1)
    """jsonPath = (str(Path.home()) +
                "/G88.2024.T05.GE2/Arrival.json")
    result2 = hotel.guestArrival(jsonPath)
    result3 = hotel.guestCheckout('e21263a92c0651e895a03558af54cf71399af99094e0f041063ed8c676241355')
    print(result3)"""








if __name__ == "__main__":
    main()
