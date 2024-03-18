from UC3MTravel.HotelReservation import HotelReservation
from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManagementException import HotelManagementException
from UC3MTravel.HotelStay import HotelStay

import datetime
import json
import hashlib

# FIRST FUNCTION
def room_reservation (credit_card, name_surname, id_Card, phone_number,
                      room_type, arrival_date, num_days):

    hotel = HotelManager()

    # PROCESS 1 (Check Inputs)
    # Credit_card
    #Check if it is the correct format
    credit_card = str(credit_card)
    if (credit_card.isdigit() == False) or len(credit_card) != 16:
        raise HotelManagementException("Invalid credit card format")
    # Check if the number is valid
    if hotel.validatecreditcard(credit_card) == False:
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
    reservation = HotelReservation(id_Card, credit_card, name_surname, phone_number, room_type, num_days)
    localizer = reservation.LOCALIZER

    # PROCESS 3 (Store data in JSON file)
    # Remove the "HotelReservation:" prefix and replace single quotes with double quotes
    json_string = str(reservation).replace("HotelReservation:", "").replace(
        "'", '"')
    # Convert the JSON string into a Python dictionary
    reservation_data = json.loads(json_string)
    # Try to load existing data
    try:
        with open('Reservations.json', 'r') as f:
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
    with open('Reservations.json', 'w') as f:
        json.dump(existing_data, f, indent=4)

    # We return the localizer
    return localizer









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

    """result = room_reservation(5555555555554444,
                              "Marta Pomelo",
                              1236,
                              561321141,
                              "single",
                              "15/07/2024",
                              5)
    print(result)"""
    """print(check_localizer("898846d21b4246c21367b6021324498a"))
    print(check_localizer("4525f9f947b84e562153ff5216fd1e79"))
    print(check_localizer("4525f9f947b84e562153ff5216fd1e7"))
    print(check_localizer("4525f9f947b84e562153ff5216fd4e79"))
    """


    # Define the relative path to the file
    file_path = './Arrival.json'
    result = guest_arrival(file_path)
    print(result)


if __name__ == "__main__":
    main()
