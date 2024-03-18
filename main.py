#THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
#IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS.

from UC3MTravel import HotelManager

def main():
    # MAIN PROGRAM
    Hotel = HotelManager()
    result = Hotel.room_reservation(5555555555554444,
                                    "Marta Pomelo",
                                    1236,
                                    561321141,
                                    "single",
                                    "15/07/2024",
                                    5)
    print(result)



    mng = HotelManager()
    res = mng.ReaddatafromJSOn("test.json")
    strRes = res.__str__()
    print(strRes)
    print("CreditCard: " + res.CREDITCARD)
    print(res.LOCALIZER)






if __name__ == "__main__":
    main()
