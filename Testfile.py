"""File with all the tests of each function"""
import json
from datetime import datetime
import unittest
from freezegun import freeze_time
from UC3MTravel import hotelManagementException
from UC3MTravel.HotelManager import HotelManager

class testRoomReservation(unittest.TestCase):
    """Test cases for the first function"""

    def testTc1Valid(self):
        """Valid case in which all the information is correct and the person
        does not already have a reservation"""

        myManager = HotelManager()
        info = (5555555555554444, "Santiago P", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC1Valid
        value = myManager.room_reservation(*info)
        self.assertEqual(value, 'ea0a2dcb07062ade04d6b9097ae096b1')

    def testTc2(self):
        """Invalid case in which all the information is correct but the person
        already has a reservation"""

        myManager = HotelManager()
        info = (5555555555554444, "Santiago P", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.room_reservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), info[1] + " already has a reservation")

class testGuestArrival(unittest.TestCase):
    """Test cases for the second function"""
    @freeze_time("2024/03/18")
    def testTc1Valid(self):
        """Valid case in which all the information is correct"""

        myManager = HotelManager()
        filePath = "JSONtestsFunction2/TC1Valid.json"  # Use the file
        # TC1Valid.json
        value = myManager.guest_arrival(filePath)
        self.assertEqual(value, '256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6')

    def testTc2(self):
        """Test for the second case, empty file"""
        # JSON empty file name
        myManager = HotelManager()
        filePath = "JSONtestsFunction2/TC2.json"
        exception = None
        try:
            myManager.guest_arrival(filePath)
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
        myManager = HotelManager()
        filePath = "JSONtestsFunction2/TC3.json"
        exception = None
        try:
            myManager.guest_arrival(filePath)
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
        myManager = HotelManager()
        filePath = "JSONtestsFunction2/TC4.json"
        exception = None
        try:
            myManager.guest_arrival(filePath)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc5(self):
        """Test for the fifth case, empty data"""
        # JSON empty file name
        myManager = HotelManager()
        filePath = "JSONtestsFunction2/TC5.json"
        exception = None
        try:
            myManager.guest_arrival(filePath)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "'Localizer' key missing in JSON")
    def testTc6(self):
        """Test for the sixth case, duplicated data"""
        myManager = HotelManager()
        filePath = "JSONtestsFunction2/TC6.json"  # Use the file test.json
        value = myManager.guest_arrival(filePath)
        self.assertEqual(value,
                         '256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6')
    def testTc7F1DEL(self):
        """Test for the seventh case, one of the fields is deleted. In this
        case only F1."""

        fileName = "JSONtestsFunction2/TC7F1.json"  # JSON empty file name
        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
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
        fileName = "JSONtestsFunction2/TC7F2.json"
        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "'Id' key missing in JSON")
    def testTc8F1DUP(self):
        """Test for the seventh case, one of the fields is duplicated"""
        # JSON name
        fileName = "JSONtestsFunction2/TC8.json"
        myManager = HotelManager()
        value = myManager.guest_arrival(fileName)
        self.assertEqual(value, '256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6')

    def testTc9MOD(self):
        """Test for the ninth case, separator is modified"""

        # JSON file name
        fileName = "JSONtestsFunction2/TC9.json"
        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
    def testTc9DUP(self):
        """Test for the ninth case, separator is duplicated"""

        # JSON file name
        fileName = "JSONtestsFunction2/TC9.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")

    def testTc10DUP(self):
        """Test for the tenth case, data1 or value1 duplicated or deleted. We
        only need to test one of the cases (data1 or value1 / DEL OR DUP)"""

        # JSON file name
        fileName = "JSONtestsFunction2/TC10.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
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
        fileName = "JSONtestsFunction2/TC11.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
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
        fileName = "JSONtestsFunction2/TC12.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
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
        fileName = "JSONtestsFunction2/TC12.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
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
        fileName = "JSONtestsFunction2/TC13.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
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
        fileName = "JSONtestsFunction2/TC14.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
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
        fileName = "JSONtestsFunction2/TC15.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
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
        fileName = "JSONtestsFunction2/TC16.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
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
        fileName = "JSONtestsFunction2/TC17.json"

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "new IdCard is not in reservation")

if __name__ == '__main__':
    unittest.main()
