
from UC3MTravel.HotelReservation import HotelReservation
from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManagementException import HotelManagementException
from UC3MTravel.HotelStay import HotelStay

import json
import hashlib

# SECOND FUNCTION
def guest_arrival (file_path):

    # First process of the function
    try:
        # Open the JSON file and load its contents
        with open(file_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or is empty, return False
        return False
    # Check if 'Localizer' key exists in the data
    localizer_found = False
    localizer = " "
    for item in data:
        if 'Localizer' in item:
            localizer_found = True
            localizer = item['Localizer']
            break

    if not localizer_found:
        raise HotelManagementException("'Localizer' key missing in JSON")
    # Check if the length of the localizer is correct (32 hexadecimal characters)
    correct = check_localizer(localizer)
    if correct:
        print("information provided with respect to the localizer is GOD")
    # Now we need to check if the locator info is correct (idCard)
        try:
            with open('Reservations.json', 'r') as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or is empty, return False
            return False

        # Check if a reservation exists with the same localizer

        # 1. load in id the idCard from Arrival
        id_found = False
        id = " "
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




# FUNCTION TO PROVE IF THE LOCALIZER EXISTS
def check_localizer(localizer):
    # Check if the localizer is in the correct format
    if not isinstance(localizer, str) or len(localizer) != 32:
        return False

    # Try to load existing data
    try:
        with open('Reservations.json', 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or is empty, return False
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
    result = guest_arrival(file_path)
    print(result)


if __name__ == "__main__":
    main()
