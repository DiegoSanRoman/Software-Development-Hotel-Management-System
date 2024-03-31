"""This is the module storing all the information about the three functions
to be implemented, as well as the functions."""

import json
import hashlib
from datetime import datetime
from datetime import timedelta
from pathlib import Path
from src.main.python.UC3MTravel.HotelManagementException import hotelManagementException
from src.main.python.UC3MTravel.HotelReservation import hotelReservation
from src.main.python.UC3MTravel.HotelStay import hotelStay

class hotelManager:
    """Class with the three functions needed to implement."""
    def __init__(self):
        pass

    def validatecreditcard(self, x):
        """Method to check if the creditcard info is correct Assignment 2.1"""

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

    def readdatafromJSOn(self, fi):
        """Used to decode and read a json file."""
        try:
            with open(fi, encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise hotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise hotelManagementException("JSON Decode Error - Wrong JSON "
                                           "Format") from e

        firstItem = data[0]
        try:
            c = firstItem["CreditCard"]
            p = firstItem["phoneNumber"]
            req = hotelReservation(id_card="12345678Z", credit_card=c,
                                   name_surname="John Doe", phonenumber=p,
                                   room_type="single",
                                   arrival_date="04/06/2034", numdays=3)
        except KeyError as e:
            raise hotelManagementException(
                "JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise hotelManagementException("Invalid credit card number")

        # Close the file
        return req

    # FIRST FUNCTION
    def roomReservation(self, credit_card, name_surname, id_card,
                         phone_number, room_type, arrival_date, num_days):
        """First function to implement, related with the reservation of a
        room"""
        # PROCESS 1 (Check Inputs)
        # Credit_card
        # Check if it is the correct format
        creditCard = str(credit_card)
        if (creditCard.isdigit() is False) or len(creditCard) != 16:
            raise hotelManagementException("Invalid credit card format")
        # Check if the number is valid
        if self.validatecreditcard(creditCard) is False:
            raise hotelManagementException("Invalid credit card number")

        # name_surname
        # Check that the length of the string is correct
        if len(name_surname) < 10 or len(name_surname) > 50:
            raise hotelManagementException("Invalid name and surname")
        # Check that the string contains at least two strings separated by a space
        strings = name_surname.split()
        if len(strings) < 2:
            raise hotelManagementException("Invalid name and surname")

        # id_Card
        # Check that the card id has 3 digits
        idCard = str(id_card)
        if len(idCard) != 3:
            raise hotelManagementException("Invalid ID card (3 digits needed")

        # phone_number
        phoneNumber = str(phone_number)
        if len(phoneNumber) != 9:
            raise hotelManagementException("Invalid phone number")

        # room_type
        if room_type not in ["single", "double", "suite"]:
            raise hotelManagementException("Invalid room type")

        # arrival_date
        if len(arrival_date) != 10:
            raise hotelManagementException("Invalid arrival date format")
        parts = arrival_date.split('-')
        if len(parts) != 3:
            raise hotelManagementException("Invalid arrival date format")
        if not all(part.isdigit() for part in parts):
            raise hotelManagementException("Invalid arrival date format")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        if day < 1 or day > 31:
            raise hotelManagementException("Invalid day in arrival date")
        if month < 1 or month > 12:
            raise hotelManagementException("Invalid month in arrival date")
        currentYear = datetime.now().year
        if year < currentYear or year > 9999:
            raise hotelManagementException("Invalid year in arrival date")

        # num_days
        if num_days < 1 or num_days > 10:
            raise hotelManagementException("Invalid number of days")

        # If we have reached this point, it means that all inputs are correct
        idCard = int(idCard)
        # PROCESS 2 (Create reservation)
        reservation = hotelReservation(idCard, creditCard, name_surname,
                                       phoneNumber, room_type,
                                       arrival_date, num_days)
        localizer = reservation.localizer

        # PROCESS 3 (Store data in JSON file)
        # Remove the "HotelReservation:" prefix and replace single quotes with double quotes
        jsonString = str(reservation).replace("HotelReservation:","").replace(
            "'", '"')
        # Convert the JSON string into a Python dictionary
        reservationData = json.loads(jsonString)
        # Try to load existing data
        jsonPath = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForFunctions/Reservations.json"
        try:
            with open(jsonPath, 'r', encoding='utf-8') as f:
                existingData = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or is empty, initialize existing_data as an empty list
            existingData = []
        # Check if a reservation already exists for the same person
        for existingReservation in existingData:
            # Check if the name and surname match
            if existingReservation.get('name_surname') == name_surname:
                raise hotelManagementException(f"{name_surname} already has a "
                                               "reservation")
        # Append new reservation data
        existingData.append(reservationData)
        # Write updated data back to file
        with open(jsonPath, 'w', encoding='utf-8') as f:
            json.dump(existingData, f, indent=4)

        # We return the localizer
        return localizer

    def guestArrival(self, file_path):
        """This is the second function of the assignment and it corresponds to
            the arrival of the guest to the hotel, where we need to check if he/she
            is actually the expected guest and all the info is correct"""
        # First we open both json files (data, existing_data)
        jsonPath1 = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForFunctions/Reservations.json"
        try:
            # Open the JSON file and load its contents
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            # If the file does not exist or is empty, raise a custom exception
            raise hotelManagementException("File not found or empty file") \
                from exc
        try:
            with open(jsonPath1, 'r', encoding='utf-8') as f:
                existingData = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            # If the file does not exist or is empty, return False
            raise hotelManagementException("File not found or empty file") \
                from exc
        # Check if 'Localizer' key exists in the data
        localizerFound = False
        localizer = " "
        idNum = " "
        for item in data:
            if 'Localizer' in item:
                localizerFound = True
                localizer = item['Localizer']
                break

        if not localizerFound:
            raise hotelManagementException("'Localizer' key missing in JSON")
        # Check if the length of the localizer is correct (32 hexadecimal characters)
        correct = self.checkLocalizer(localizer, existingData)
        if correct == 0:
            raise hotelManagementException("'Localizer' is not well defined")
        # Now we need to check if the locator info is correct (idCard)
        # 1. load in id the idCard from Arrival
        idFound = False
        for item in data:
            if 'IdCard' in item:
                idFound = True
                idNum = item['IdCard']
                break
        if not idFound:
            raise hotelManagementException("'Id' key missing in JSON")
        # NOW CHECK IF THE ID OF BOTH JSON FILES IS THE SAME
        idCorrect = False
        if idNum == correct:
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
            if (idNum == item['id_card']) and ('room_type' in item and
                                              'num_days'
                    in item and 'arrival_date' in item):
                founded = True
                roomtype = item['room_type']
                numdays = item['num_days']
                arrival = item['arrival_date']
                break
        print(roomtype, numdays, arrival)
        if not founded:
            hotelManagementException("Number of days or room type or arrival_date "
                "are missing in the guest's info")
        # Now we create an instance of HotelStay
        myStay = hotelStay(idNum, localizer, numdays, roomtype)
        print(arrival, myStay.arrival)
        if arrival == myStay.arrival:
                # Remove the "HotelReservation:" prefix and replace single quotes with double quotes
            jsonString = myStay.signature_string().replace(
                "HotelReservation:","").replace("'", '"')
            # Convert the JSON string into a Python dictionary
            reservationData = json.loads(jsonString)
            jsonPath2 = str(Path.home()) + \
                           "/G88.2024.T05.GE2/src/JSONfiles" \
                           "/JsonForFunctions/Stay.json"
            # We write in a json file all info related to the hotelStay
            try:
                with open(jsonPath2, 'r', encoding='utf-8') as f:
                    stayData = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                # If the file does not exist or is empty, initialize existing_data as an empty list
                stayData = []
            stayData.append(reservationData)
            # Write updated data back to file
            with open(jsonPath2, 'w', encoding='utf-8') as f:
                json.dump(stayData, f)
            print(f"Room key: {myStay.roomKey}")
            return myStay.roomKey

    # FUNCTION TO PROVE IF THE LOCALIZER EXISTS
    def checkLocalizer(self, localizer, existing_data):
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
    def guestCheckout(self, room_key):
        """This third function receives a room key (64-character-long string
        in hexadecimal) and checks that it corresponds to a reservation in
        our hotel. It also checks that the checkout is being held the day it
        was scheduled. If both things are correct, it returns True and saves
        into a file the departure timestamp and the room key value."""

        # We check if the key is processable (sha256 type)
        if len(room_key) != 64:
            raise hotelManagementException("Not processable room code.")
        for c in room_key:
            if c not in '0123456789abcdefABCDEF':
                raise hotelManagementException("Not processable room code.")

        # The key is processable. Now we check if it is valid. To do so, we compare the key provided to the keys generated by each of our
        # reservations.
        jsonPath1 = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForFunctions/Reservations.json"
        jsonPath2 = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForFunctions/Arrival.json"
        try:
            # Open the JSON file and load its contents.
            with open(jsonPath1, 'r', encoding='utf-8') as f:
                reservationsData = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            # If the file does not exist or it is empty, we raise an error.
            raise hotelManagementException(
                "Reservations file not found or it is empty.") from exc
        try:
            # Open the JSON file and load its contents.
            with open(jsonPath2, 'r', encoding='utf-8') as f:
                arrivalData = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            # If the file does not exist or it is empty, we raise an error.
            raise hotelManagementException(
                "Arrivals file not found or it is empty.") from exc

        auxLocalizer, auxId, auxArrival, auxDays, auxRoom = 0, 0, 0, 0, 0
        validKey = False
        for item in arrivalData:
            localizerFound, allDataRetrieved = False, False
            if not localizerFound and 'Localizer' in item and "IdCard" in item:
                auxLocalizer = item['Localizer']
                auxId = item['IdCard']
                localizerFound = True

            if localizerFound:
                for item2 in reservationsData:
                    if not allDataRetrieved and 'id_card' in item2 and item2[
                        'id_card'] == auxId:
                        auxDays = item2['num_days']
                        auxRoom = item2['room_type']
                        auxArrival = item2["arrival_date"]
                        allDataRetrieved = True

            if allDataRetrieved:
                auxStay = hotelStay(auxId, auxLocalizer, auxDays, auxRoom)
                auxKey = hashlib.sha256(
                    auxStay.signature_string().encode()).hexdigest()
                print(auxKey)
                if auxKey == room_key:
                    print('Valid key')
                    validKey = True
                    break

        if not validKey:
            raise hotelManagementException("Key is not registered.")

        # At this point, we know that the key is valid. Now let's check that the departure date is valid. To do so, we will calculate the departure
        # date planned in Reservations.json (arrival_date + num_days) and compare it to the current date (only taking the year, month and day into
        # account).

        arrivalDate = datetime.strptime(auxArrival, '%Y-%m-%d')
        departureDate = arrivalDate + timedelta(days=auxDays)
        time1 = departureDate.strftime('%Y-%m-%d')

        timeNow = datetime.utcnow()
        time2 = timeNow.strftime('%Y-%m-%d')
        print(time1, time2)
        if time1 != time2:
            raise hotelManagementException("Departure date is not valid.")

        # Now we must save into a file the timestamp of the departure (UTC time) and the room key value.
        jsonString = {"departure": time2,
                       "room_key": room_key}
        jsonPath3 = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForFunctions/checkOut.json"
        try:
            with open(jsonPath3, 'r', encoding='utf-8') as f:
                checkoutData = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or is empty, initialize existing_data as an empty list
            checkoutData = []
        checkoutData.append(jsonString)
        # Write updated data back to file
        with open(jsonPath3, 'w', encoding='utf-8') as f:
            json.dump(checkoutData, f, indent=4)
        return True
