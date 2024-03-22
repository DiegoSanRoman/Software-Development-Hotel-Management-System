"""For now, we are using this file to record information about the functions
of GE2. Then we will store those functions in HotelManager"""
from datetime import datetime
import json
import hashlib
from UC3MTravel.HotelReservation import HotelReservation
from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManagementException import HotelManagementException
from UC3MTravel.HotelStay import hotelStay


# SECOND FUNCTION
def guest_arrival(file_path):
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
    correct = check_localizer(localizer, existingData)
    if not correct:
        raise HotelManagementException("'Localizer' is not well defined")
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
        raise HotelManagementException("new IdCard is not in reservation")
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
    print(roomtype, numdays, arrival)
    if not founded:
        HotelManagementException("Number of days or room type or arrival_date "
                                 "are missing in the guest's info")

# FUNCTION TO PROVE IF THE LOCALIZER EXISTS
def check_localizer(localizer, existingdata):
    """This is a function whose objective is to check if the localizer is
    correct and there is already a reservation with that localizer"""
    # Check if the localizer is in the correct format
    if not isinstance(localizer, str) or len(localizer) != 32:
        return False

    # Check if a reservation exists with the same localizer
    for reservation in existingdata:
        # Remove the "HotelReservation:" prefix and replace single quotes with double quotes
        jsonString = str(reservation).replace("HotelReservation:","").replace("'", '"')
        # Generate the MD5 hash of the reservation data
        reservationHash = hashlib.md5(jsonString.encode()).hexdigest()
        # If the hashes match, return True
        if reservationHash == localizer:
            return True

    # If no matching reservation was found, return False
    return False

# Main
def main():
    """A main created to try and see if the function works"""
    # Define the relative path to the file
    filePath = './Arrival.json'
    guest_arrival(filePath)


if __name__ == "__main__":
    main()