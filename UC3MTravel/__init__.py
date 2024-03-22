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
        with open(file_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or is empty, return False
        return False
    try:
        with open('Reservations.json', 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or is empty, return False
        return False
    # Check if 'Localizer' key exists in the data
    localizer_found = False
    localizer = " "
    id = " "
    for item in data:
        if 'Localizer' in item:
            localizer_found = True
            localizer = item['Localizer']
            break

    if not localizer_found:
        raise HotelManagementException("'Localizer' key missing in JSON")
    # Check if the length of the localizer is correct (32 hexadecimal characters)
    correct = check_localizer(localizer, existing_data)
    if correct:
        print("information provided with respect to the localizer is GOD")
    # Now we need to check if the locator info is correct (idCard)
        # 1. load in id the idCard from Arrival
        id_found = False
        for item in data:
            if 'IdCard' in item:
                id_found = True
                id = item['IdCard']
                break
        if not id_found:
            raise HotelManagementException("'Id' key missing in JSON")

        # NOW CHECK IF THE ID OF BOTH JSON FILES IS THE SAME
        id_correct = False
        for reservation in existing_data:
            if reservation["id_card"] == id:
                id_correct = True
                break
        if not id_correct:
            raise HotelManagementException("new IdCard is not in reservation")
        else:
            print("All the info of the new locator is correct")
    # SECOND PART OF THE FUNCTION
    # First we charge numdays and roomtype from reservations.json
    roomtype = " "
    numdays = " "
    arrival = " "
    founded = False
    for item in existing_data:
        if item['id_card'] == id:
            if 'room_type' in item and 'num_days' in item and 'arrival_date ' \
                                                              'in item':
                founded = True
                roomtype = item['room_type']
                numdays = item['num_days']
                arrival = item['arrival_date']
                break
    if not founded:
        HotelManagementException("Number of days or room type or arrival_date "
                                 "are missing in the guest's info")

    # NOW WE CREATE AN STAY INSTANCE
    mystay = hotelStay(id, localizer, numdays, roomtype)

    """FINALLY WE NEED TO CHECK THAT THE ARRIVAL DATE PROVIDED IS IN AN 
    EXISTING RESERVATION"""
    good_arrival = datetime.fromtimestamp(arrival)

    if mystay.arrival == good_arrival:
        print("All information is correct")
        return mystay.room_key







# FUNCTION TO PROVE IF THE LOCALIZER EXISTS
def check_localizer(localizer, existing_data):
    # Check if the localizer is in the correct format
    if not isinstance(localizer, str) or len(localizer) != 32:
        return False

    # Check if a reservation exists with the same localizer
    for reservation in existing_data:
        # Remove the "HotelReservation:" prefix and replace single quotes with double quotes
        json_string = str(reservation).replace("HotelReservation:", "").replace("'", '"')
        # Generate the MD5 hash of the reservation data
        reservation_hash = hashlib.md5(json_string.encode()).hexdigest()
        # If the hashes match, return True
        if reservation_hash == localizer:
            return True

    # If no matching reservation was found, return False
    return False

# Main
def main():
    # Define the relative path to the file
    file_path = './Arrival.json'
    guest_arrival(file_path)


if __name__ == "__main__":
    main()
