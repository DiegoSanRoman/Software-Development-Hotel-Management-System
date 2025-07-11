"""File with all the tests of each function"""
import unittest
import json
from freezegun import freeze_time
from pathlib import Path
from UC3MTravel.HotelManagementException import hotelManagementException
from UC3MTravel.HotelManager import hotelManager
from UC3MTravel.HotelReservation import hotelReservation

# Before starting the tests we need to ensure that we have a valid
# reservation in the json file:
resPath = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForFunctions/Reservations.json"

jsonInfo = {
                    "id_card": 100,
                    "name_surname": "Santiago P",
                    "credit_card": 5555555555554444,
                    "phone_number:": 100000000,
                    "arrival_date": "2024-01-01",
                    "num_days": 1,
                    "room_type": "single",
                    }
jsonString = str(jsonInfo).replace("HotelReservation:", "").replace(
            "'", '"')
# We charge the string in JSON format
reservationData = json.loads(jsonString)
# We open the reservations.json and append the new data
try:
    with open(resPath, 'r', encoding='utf-8') as f:
                existingData = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    # If the file does not exist or is empty, initialize existing_data as an empty list
    existingData = []
existingData.append(reservationData)
# Write updated data back to file
with open(resPath, 'w', encoding='utf-8') as f:
    json.dump(existingData, f, indent=4)

class TestGuestArrival(unittest.TestCase):
    """Test cases for the second function"""
    @freeze_time('2024-01-01')
    def testTc1Valid(self):
        """Valid case in which all the information is correct. We write the
        info in reservations in order not to have problems with the
        localizer."""

        myManager = hotelManager()
        testpath = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC1Valid.json"
        value = myManager.guestArrival(testpath)
        self.assertEqual(value, '3698305d5a45eded7ed2d2f504f2fbfaa80bcf1bfb0b3e2e33215407addc752f')

    def testTc2(self):
        """Test for the second case, empty file"""
        # JSON empty file name
        myManager = hotelManager()
        filePath = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC2.json"
        exception = None
        try:
            myManager.guestArrival(filePath)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc3(self):
        """Test for the second case, duplicated files FileFile (without
        separator)"""
        # JSON empty file name
        myManager = hotelManager()
        filePath = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC3.json"
        exception = None
        try:
            myManager.guestArrival(filePath)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc4(self):
        """Test for the 4th case, DEL/MOD/DUP. In this case we just check
        MOD, since with the other two the result will be the same.)"""
        # JSON empty file name
        myManager = hotelManager()
        filePath = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC4.json"
        exception = None
        try:
            myManager.guestArrival(filePath)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc5(self):
        """Test for the fifth case, empty data"""
        # JSON empty file name
        myManager = hotelManager()
        filePath = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC5.json"
        exception = None
        try:
            myManager.guestArrival(filePath)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "'Localizer' key missing in JSON")

    @freeze_time('2024-01-01')
    def testTc6(self):
        """Test for the sixth case, duplicated data"""
        myManager = hotelManager()
        filePath = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC6.json"  # Use the file test.json
        value = myManager.guestArrival(filePath)
        self.assertEqual(value,
                         '3698305d5a45eded7ed2d2f504f2fbfaa80bcf1bfb0b3e2e33215407addc752f')
    def testTc7F1DEL(self):
        """Test for the seventh case, one of the fields is deleted. In this
        case only F1."""

        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC7F1.json"  # JSON empty file name
        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "'Localizer' key missing in JSON")
    def testTc7F2DEL(self):
        """Test for the seventh case, one of the fields is deleted, in this
        case F2."""

        # JSON name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC7F2.json"
        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "'Id' key missing in JSON")
    @freeze_time('2024-01-01')
    def testTc8F1DUP(self):
        """Test for the seventh case, one of the fields is duplicated"""
        # JSON name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC8.json"
        myManager = hotelManager()
        value = myManager.guestArrival(fileName)
        self.assertEqual(value, '3698305d5a45eded7ed2d2f504f2fbfaa80bcf1bfb0b3e2e33215407addc752f')

    def testTc9MOD(self):
        """Test for the ninth case, separator is modified"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC9.json"
        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc9DUP(self):
        """Test for the ninth case, separator is duplicated"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC9.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")

    def testTc10DUP(self):
        """Test for the tenth case, data1 duplicated or deleted. We
        only need to test one of the cases (data1 or value1 / DEL OR DUP)"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC10.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")

    def testTc11DEL(self):
        """Test for the eleventh case, data2 or value2 duplicated or
        deleted. We only need to test one of the cases (data2 or value2 /
        DEL OR DUP)"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC11.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc12MOD(self):
        """Test for the eleventh case, data2 or value2 duplicated or
        deleted. We only need to test one of the cases (data2 or value2 /
        DEL OR DUP), and only one json for all cases (result is the same)"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC12.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc12DUP(self):
        """Test for the 12th case, equality duplicated or
        modified. We only need to test one of the cases (MOD OR DUP), and
        only one json for all cases (result is the same)"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC12.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc13(self):
        """Test for the 13th case, any operation related with quotes. We only
        need to test one of the cases (MOD/DUP/DEL) in any of the fields,and
        only one json for all cases (result is the same)"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC13.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc14(self):
        """Test for the 14th case, any operation related with Localizer key. We
        only need to test one of the cases (MOD/DUP/DEL), and only one json
        for all cases (result is the same)"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC14.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "'Localizer' key missing in JSON")
    def testTc15(self):
        """Test for the 15th case, any operation related with Id key. We
        only need to test one of the cases (MOD/DUP/DEL), and only one json
        for all cases (result is the same)"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC15.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "'Id' key missing in JSON")
    def testTc16(self):
        """Test for the 16th case, any operation related with Localizer
        value. We only need to test one of the cases (MOD/DUP/DEL), and only
        one json for all cases (result is the same)"""

        # JSON file name
        fileName = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC16.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "'Localizer' is not well defined")
    def testTc17(self):
        """Test for the 17th case, any operation related with Id value. We
        only need to test one of the cases (MOD/DUP/DEL), and only one json
        for all cases (result is the same). Consider DEL as putting value 0"""

        # JSON file name
        filename = str(Path.home()) + \
                   "/G88.2024.T05.GE2/src/JSONfiles" \
                   "/JsonForTests/TC17.json"

        myManager = hotelManager()
        exception = None
        try:
            myManager.guestArrival(filename)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "new IdCard is not in reservation")
if __name__ == '__main__':
    unittest.main()
