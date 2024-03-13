import json
from HotelManagementException import HotelManagementException
from HotelReservation import HotelReservation

class HotelManager:
    def __init__(self):
        pass

    def validatecreditcard( self, x ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE

        # Step 1: Transform the 16-digit number to a list containing the digits
        # of the number
        numbers = [int(digit) for digit in str(x)]

        # Step 2: Double every second digit starting from the right
        # according to the Luhn algorithm
        for i in range(len(numbers) - 2, -1, -2):
            numbers[i] *= 2
            if numbers[i] > 9:
                numbers[i] -= 9

        # Step 3: Sum all the digits
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]

        # Step 4: Check if the total module 10 is equal to 0. If it is,
        # then the credit card number is correct, and we return True. If it
        # is not, then the credit card number is incorrect, and we return
        # False.
        return total % 10 == 0

    def ReaddatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req