import json
from datetime import datetime, timedelta
import hashlib
from UC3MTravel.HotelManagementException import hotelManagementException
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
            raise hotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise hotelManagementException("JSON Decode Error - Wrong JSON "
                                           "Format") from e

        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z", creditcardNumb=c,
                                   nAMeAndSURNAME="John Doe", phonenumber=p,
                                   room_type="single", arrival_date =
                                   "04/06/2034", numdays=3)
        except KeyError as e:
            raise hotelManagementException(
                "JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise hotelManagementException("Invalid credit card number")

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
            raise hotelManagementException("Invalid credit card format")
        # Check if the number is valid
        if self.validatecreditcard(credit_card) == False:
            raise hotelManagementException("Invalid credit card number")

        # name_surname
        # Check that the length of the string is correct
        if len(name_surname) < 10 or len(name_surname) > 50:
            raise hotelManagementException("Invalid name and surname length")
        # Check that the string contains at least two strings separated by a space
        strings = name_surname.split()
        if len(strings) < 2:
            raise hotelManagementException("Invalid name and surname format")

        # id_Card
        # Check that the card id has 3 digits
        id_Card = str(id_Card)
        if len(id_Card) != 3:
            raise hotelManagementException("Invalid ID card (3 digits needed)")

        # phone_number
        phone_number = str(phone_number)
        if len(phone_number) != 9:
            raise hotelManagementException("Invalid phone number")

        # room_type
        if room_type not in ["single", "double", "suite"]:
            raise hotelManagementException("Invalid room type")

        # arrival_date
        if len(arrival_date) != 10:
            raise hotelManagementException("Invalid arrival date format")
        parts = arrival_date.split('/')
        if len(parts) != 3:
            raise hotelManagementException("Invalid arrival date format")
        if not all(part.isdigit() for part in parts):
            raise hotelManagementException("Invalid arrival date format")
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
        if day < 1 or day > 31:
            raise hotelManagementException("Invalid day in arrival date")
        if month < 1 or month > 12:
            raise hotelManagementException("Invalid month in arrival date")
        current_year = datetime.datetime.now().year
        if year < current_year or year > 9999:
            raise hotelManagementException("Invalid year in arrival date")

        # num_days
        if num_days < 1 or num_days > 10:
            raise hotelManagementException("Invalid number of days")

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
                raise hotelManagementException(
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
            raise hotelManagementException("File not found or empty file")
        try:
            with open('../Reservations.json', 'r', encoding='utf-8') as f:
                existingData = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or is empty, return False
            raise hotelManagementException("File not found or empty file")
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
            raise hotelManagementException("'Localizer' key missing in JSON")
        # Check if the length of the localizer is correct (32 hexadecimal characters)
        correct = self.check_localizer(localizer, existingData)
        if correct == 0:
            raise hotelManagementException("'Localizer' is not well defined")
        # Now we need to check if the locator info is correct (idCard)
        # 1. load in id the idCard from Arrival
        idFound = False
        for item in data:
            if 'IdCard' in item:
                idFound = True
                id = item['IdCard']
                break
        if not idFound:
            raise hotelManagementException("'Id' key missing in JSON")
        # NOW CHECK IF THE ID OF BOTH JSON FILES IS THE SAME
        idCorrect = False
        if id == correct:
            idCorrect = True
        if not idCorrect:
            raise hotelManagementException("new IdCard is not in reservation")
        # SECOND PART OF THE FUNCTION
        # First we charge numdays, roomtype and arrival from reservations.json
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
        print(roomtype, numdays, arrival)
        if not founded:
            hotelManagementException(
                "Number of days or room type or arrival_date "
                "are missing in the guest's info")
        # Now we create an instance of HotelStay
        myStay = hotelStay(id, localizer, numdays, roomtype)
        if arrival == myStay.arrival:
            if arrival == myStay.arrival:
                # Remove the "HotelReservation:" prefix and replace single quotes with double quotes
                json_string = myStay.signature_string().replace(
                    "HotelReservation:",
                    "").replace(
                    "'", '"')
                # Convert the JSON string into a Python dictionary
                reservation_data = json.loads(json_string)
                # We write in a json file all info related to the hotelStay
                try:
                    with open('../Stay.json', 'r') as f:
                        stayData = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    # If the file does not exist or is empty, initialize existing_data as an empty list
                    stayData = []
                stayData.append(reservation_data)
                # Write updated data back to file
                with open('../Stay.json', 'w') as f:
                    json.dump(stayData, f)
            print("Room key: %s" % myStay.roomKey)
            return myStay.roomKey

    # FUNCTION TO PROVE IF THE LOCALIZER EXISTS
    def check_localizer(self, localizer, existing_data):
        """This is a function whose objective is to check if the localizer is
        correct and there is already a reservation with that localizer"""
        # Check if the localizer is in the correct format
        if not isinstance(localizer, str) or len(localizer) != 32:
            return 0

        # Check if a reservation exists with the same localizer
        for reservation in existing_data:
            # Remove the "HotelReservation:" prefix and replace single quotes with double quotes
            jsonString = str(reservation).replace("HotelReservation:",
                                                  "").replace("'", '"')
            # Generate the MD5 hash of the reservation data
            reservationHash = hashlib.md5(jsonString.encode()).hexdigest()
            # If the hashes match, return True
            if reservationHash == localizer:
                return reservation["id_card"]

        # If no matching reservation was found, return False
        return 0

    # THIRD FUNCTION
    def guest_checkout(self, room_key):
        """This third function receives a room key (64-character-long string in hexadecimal) and checks that it corresponds to a reservation in
        our hotel. It also checks that the checkout is being held the day it was scheduled. If both things are correct, it returns True and saves
        into a file the departure timestamp and the room key value."""

        # We check if the key is processable (sha256 type)
        if len(room_key) != 64:
            raise hotelManagementException("Not processable room code.")
        for c in room_key:
            if c not in '0123456789abcdefABCDEF':
                raise hotelManagementException("Not processable room code.")

        # The key is processable. Now we check if it is valid. To do so, we compare the key provided to the keys generated by each of our
        # reservations.
        try:
            # Open the JSON file and load its contents.
            with open('../Reservations.json', 'r', encoding='utf-8') as f:
                reservationsData = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or it is empty, we raise an error.
            raise hotelManagementException("File not found or empty file.")
        try:
            # Open the JSON file and load its contents.
            with open('../Arrival.json', 'r', encoding='utf-8') as f:
                arrivalData = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or it is empty, we raise an error.
            raise hotelManagementException("File not found or empty file.")

        aux_localizer, aux_id, aux_days, aux_room = 0, 0, 0, 0
        valid_key = False
        for item in arrivalData:
            localizer_found, all_data_retrieved = False, False
            if not localizer_found and 'Localizer' in item and "IdCard" in item:
                aux_localizer = item['Localizer']
                aux_id = item['IdCard']
                localizer_found = True

            if localizer_found:
                for item2 in reservationsData:
                    if not all_data_retrieved and 'id_card' in item2 and item2['id_card'] == aux_id:
                        aux_days = item2['num_days']
                        aux_room = item2['room_type']
                        aux_arrival = item2["arrival_date"]
                        all_data_retrieved = True

            if all_data_retrieved:
                auxStay = hotelStay(aux_id, aux_localizer, aux_days, aux_room)
                auxKey = hashlib.sha256(auxStay.signature_string().encode()).hexdigest()
                if auxKey == room_key:
                    print('Valid key')
                    valid_key = True
                    break

        if not valid_key:
            raise hotelManagementException("Key is not registered.")

        # At this point, we know that the key is valid. Now let's check that the departure date is valid. To do so, we will calculate the departure
        # date planned in Reservations.json (arrival_date + num_days) and compare it to the current date (only taking the year, month and day into
        # account).
        arrival_date = datetime.utcfromtimestamp(aux_arrival)
        departure_date = arrival_date + timedelta(aux_days)
        time1 = departure_date.strftime('%Y-%m-%d')

        time_now = datetime.utcnow()
        time2 = time_now.strftime('%Y-%m-%d')
        if time1 != time2:
            raise hotelManagementException("Departure date is not valid.")

        # Now we must save into a file the timestamp of the departure (UTC time) and the room key value.
        json_string = {"departure": time_now,
                     "room_key": room_key}
        try:
            with open('../checkOut.json', 'r') as f:
                checkout_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or is empty, initialize existing_data as an empty list
            checkout_data = []
        checkout_data.append(json_string)
        # Write updated data back to file
        with open('../checkOut.json', 'w') as f:
            json.dump(checkout_data, f)




