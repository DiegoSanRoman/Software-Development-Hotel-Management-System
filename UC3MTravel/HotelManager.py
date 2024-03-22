import json
import datetime
import hashlib
from UC3MTravel.HotelManagementException import HotelManagementException
from UC3MTravel.HotelReservation import HotelReservation
from UC3MTravel.HotelStay import hotelStay

class HotelManager:
    def __init__(self):
        pass

    def validatecreditcard(self, x):
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

    def ReaddatafromJSOn(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON "
                                           "Format") from e

        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z", creditcardNumb=c,
                                   nAMeAndSURNAME="John Doe", phonenumber=p,
                                   room_type="single", arrival_date =
                                   "04/06/2034", numdays=3)
        except KeyError as e:
            raise HotelManagementException(
                "JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req

    # FIRST FUNCTION
    def room_reservation(self, credit_card, name_surname, id_Card,
                         phone_number, room_type, arrival_date, num_days):

        # PROCESS 1 (Check Inputs)
        # Credit_card
        # Check if it is the correct format
        credit_card = str(credit_card)
        if (credit_card.isdigit() == False) or len(credit_card) != 16:
            raise HotelManagementException("Invalid credit card format")
        # Check if the number is valid
        if self.validatecreditcard(credit_card) == False:
            raise HotelManagementException("Invalid credit card number")

        # name_surname
        strings = name_surname.split()
        if len(strings) < 2:
            raise HotelManagementException("Invalid name and surname")

        # id_Card
        # I don't know how to check this

        # phone_number
        phone_number = str(phone_number)
        if len(phone_number) != 9:
            raise HotelManagementException("Invalid phone number")

        # room_type
        if room_type not in ["single", "double", "suite"]:
            raise HotelManagementException("Invalid room type")

        # arrival_date
        if len(arrival_date) != 10:
            raise HotelManagementException("Invalid arrival date format")
        parts = arrival_date.split('/')
        if len(parts) != 3:
            raise HotelManagementException("Invalid arrival date format")
        if not all(part.isdigit() for part in parts):
            raise HotelManagementException("Invalid arrival date format")
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
        if day < 1 or day > 31:
            raise HotelManagementException("Invalid day in arrival date")
        if month < 1 or month > 12:
            raise HotelManagementException("Invalid month in arrival date")
        current_year = datetime.datetime.now().year
        if year < current_year or year > 9999:
            raise HotelManagementException("Invalid year in arrival date")

        # num_days
        if num_days < 1 or num_days > 10:
            raise HotelManagementException("Invalid number of days")

        # If we have reached this point, it means that all inputs are correct

        # PROCESS 2 (Create reservation)
        reservation = HotelReservation(id_Card, credit_card, name_surname,
                                       phone_number, room_type,
                                       arrival_date, num_days)
        localizer = reservation.LOCALIZER

        # PROCESS 3 (Store data in JSON file)
        # Remove the "HotelReservation:" prefix and replace single quotes with double quotes
        json_string = str(reservation).replace("HotelReservation:",
                                               "").replace(
            "'", '"')
        # Convert the JSON string into a Python dictionary
        reservation_data = json.loads(json_string)
        # Try to load existing data
        try:
            with open('../Reservations.json', 'r') as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or is empty, initialize existing_data as an empty list
            existing_data = []
        # Check if a reservation already exists for the same person
        for existing_reservation in existing_data:
            if existing_reservation['name_surname'] == name_surname:
                raise HotelManagementException(
                    "%s already has a reservation" % name_surname)
        # Append new reservation data
        existing_data.append(reservation_data)
        # Write updated data back to file
        with open('../Reservations.json', 'w') as f:
            json.dump(existing_data, f, indent=4)

        # We return the localizer
        return localizer

    def guest_arrival(self, file_path):
        """This is the second function of the assignment and it corresponds to
        the arrival of the guest to the hotel, where we need to check if he/she
        is actually the expected guest and all the info is correct"""

        # First we open both json files (data, existing_data)
        try:
            # Open the JSON file and load its contents
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or is empty, return False
            return False
        try:
            with open('../Reservations.json', 'r', encoding='utf-8') as f:
                existingData = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or is empty, return False
            return False
        # Check if 'Localizer' key exists in the data
        localizerFound = False
        localizer = " "
        id = " "
        for item in data:
            if 'Localizer' in item:
                localizerFound = True
                localizer = item['Localizer']
                break

        if not localizerFound:
            raise HotelManagementException("'Localizer' key missing in JSON")
        # Check if the length of the localizer is correct (32 hexadecimal characters)
        correct = self.check_localizer(localizer, existingData)
        if correct:
            print("information provided with respect to the localizer is GOD")
            # Now we need to check if the locator info is correct (idCard)
            # 1. load in id the idCard from Arrival
            idFound = False
            for item in data:
                if 'IdCard' in item:
                    idFound = True
                    id = item['IdCard']
                    break
            if not idFound:
                raise HotelManagementException("'Id' key missing in JSON")

            # NOW CHECK IF THE ID OF BOTH JSON FILES IS THE SAME
            idCorrect = False
            for reservation in existingData:
                if reservation["id_card"] == id:
                    idCorrect = True
                    break
            if not idCorrect:
                raise HotelManagementException(
                    "new IdCard is not in reservation")
        # SECOND PART OF THE FUNCTION
        # First we charge numdays and roomtype from reservations.json
        roomtype = " "
        numdays = " "
        arrival = " "
        founded = False
        for item in existingData:
            if id == item['id_card'] and 'room_type' in item and 'num_days' in \
                    item and 'arrival_date' in item:
                founded = True
                roomtype = item['room_type']
                numdays = item['num_days']
                arrival = item['arrival_date']
                break
        if not founded:
            HotelManagementException(
                "Number of days or room type or arrival_date "
                "are missing in the guest's info")
        else:
            print("bitches")

        # NOW WE CREATE AN STAY INSTANCE
        mystay = hotelStay(id, localizer, numdays, roomtype)

        # FINALLY WE NEED TO CHECK THAT THE ARRIVAL DATE IS IN A RESERVATION
        goodArrival = datetime.fromtimestamp(arrival)

        if mystay.arrival == goodArrival:
            print("All information is correct")
            return mystay.room_key

    # FUNCTION TO PROVE IF THE LOCALIZER EXISTS
    def check_localizer(self, localizer, existing_data):
        """This is a function whose objective is to check if the localizer is
        correct and there is already a reservation with that localizer"""
        # Check if the localizer is in the correct format
        if not isinstance(localizer, str) or len(localizer) != 32:
            return False

        # Check if a reservation exists with the same localizer
        for reservation in existing_data:
            # Remove the "HotelReservation:" prefix and replace single quotes with double quotes
            jsonString = str(reservation).replace("HotelReservation:",
                                                  "").replace("'", '"')
            # Generate the MD5 hash of the reservation data
            reservationHash = hashlib.md5(jsonString.encode()).hexdigest()
            # If the hashes match, return True
            if reservationHash == localizer:
                return True

        # If no matching reservation was found, return False
        return False

    # THIRD FUNCTION
    def guest_checkout(self, room_key):
        """This function receives a room key generated by function 2 (SHA256 hexadecimal string), checks that it is valid and saves into a file the
        timestamp of the departure and the room key value. It returns True is both elements are valid."""
        # We check that the key is valid...


