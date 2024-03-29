"""THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS."""

from UC3MTravel.HotelManager import HotelManager

def main():
    """Function to try and check methods and functions"""
    # MAIN PROGRAM
    hotel = HotelManager()
    """print(hotel.validatecreditcard(3379513561108795))
    result = hotel.room_reservation(5555555555554444,
                                    "Marta Pomelo",
                                    136,
                                    561321141,
                                    "single",
                                    "18/03/2024",
                                    5)
    print(result)"""
    beibe= hotel.room_reservation(5555555555554444, "Santiago P",100,
                                  100000000, "single",
                "01/09/2024", 1)
    print(beibe)



    mng = HotelManager()
    res = mng.ReaddatafromJSOn("test.json")
    strRes = str(res)
    print(strRes)
    print("CreditCard: " + res.CREDITCARD)
    print(res.LOCALIZER)






if __name__ == "__main__":
    main()
