"""File with all the tests of each function"""
import unittest
from freezegun import freeze_time
from UC3MTravel import hotelManagementException
from UC3MTravel.HotelManager import hotelManager

class testRoomReservation(unittest.TestCase):
    """Test cases for the first function"""

    def testTc1Valid(self):
        """Valid case in which all the information is correct and the person
        does not already have a reservation"""

        myManager = hotelManager()
        info = (5555555555554444, "Santiago P", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC1Valid
        value = myManager.roomReservation(*info)
        self.assertEqual(value, 'ea0a2dcb07062ade04d6b9097ae096b1')

    def testTc2(self):
        """Invalid case in which all the information is correct but the person
        already has a reservation"""

        myManager = hotelManager()
        info = (5555555555554444, "Santiago P", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), info[1] + " already has a reservation")

    def testTc3(self):
        """Invalid case in which the credit card number is not of the
        correct datatype"""

        myManager = hotelManager()
        info = ("credit_card_number", "Santiago P", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid credit card format")

    def testTc4(self):
        """Invalid case in which the credit card number is too long"""

        myManager = hotelManager()
        info = (55555555555544444, "Santiago P", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid credit card format")

    def testTc5(self):
        """Invalid case in which the credit card number is too short"""

        myManager = hotelManager()
        info = (555555555555444, "Santiago P", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid credit card format")

    def testTc6(self):
        """Invalid case in which the credit card number is with the correct
        format (16 digits) but the number is not valid"""

        myManager = hotelManager()
        info = (1234567812345678, "Santiago P", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid credit card number")

    def testTc7(self):
        """Invalid case in which the name and surname are of the incorrect
        datatype"""

        myManager = hotelManager()
        info = (5555555555554444, 56.78, 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid name and surname format")

    def testTc8(self):
        """Invalid case in which the name and surname are separated by an
        incorrect separator (not a blank space)"""

        myManager = hotelManager()
        info = (5555555555554444, "Marta,Pombo", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid name and surname format")

    def testTc9(self):
        """Invalid case in which the person has just a name and not a
        surname"""

        myManager = hotelManager()
        info = (5555555555554444, "Dulceida", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid name and surname format")

    def testTc10(self):
        """Invalid case in which the name and surname are a very short
        string"""

        myManager = hotelManager()
        info = (5555555555554444, "Lu Tema", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid name and surname length")

    def testTc11(self):
        """Invalid case in which the name and surname are a very long
        string"""

        myManager = hotelManager()
        info = (5555555555554444, "This is a toooooooooooooooooooooooooooooo long name", 100, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid name and surname length")

    def testTc12(self):
        """Invalid case in which the id card is of the incorrect datatype"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", "cool_number", 100000000,
                "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid ID card")

    def testTc13(self):
        """Invalid case in which the id card has 4 digits (instead of 3)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 7777, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid ID card")

    def testTc14(self):
        """Invalid case in which the id card has only two digits (instead of
        3)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 33, 100000000, "single",
                "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid ID card")

    def testTc15(self):
        """Invalid case in which the phone number is of the incorrect datatype"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, "phonenumber",
                "single", "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid phone number")

    def testTc16(self):
        """Invalid case in which the phone number has 10 digits (instead of
        9)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 7853498219,
                "single", "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid phone number")

    def testTc17(self):
        """Invalid case in which the phone number has only 8 digits (instead of 9)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 12345678,
                "single", "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid phone number")

    def testTc18(self):
        """Invalid case in which the room type is of the incorrect datatype"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                45, "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid room type")

    def testTc19(self):
        """Invalid case in which the room type is not one of the accepted
        values (single, double, suite)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "premium", "01/01/2024", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid room type")


class testRoomReservation(unittest.TestCase):
    """Test cases for the first function"""
    def testTc1Valid(self):
        """Valid case in which all the information is correct and the person
        does not already have a reservation"""

        myManager = hotelManager()
        info = (5555555555554444, "Santiago P", 100, 100000000, "single",
                "2024-01-01", 1)
        # TC1Valid
        value = myManager.roomReservation(*info)
        self.assertEqual(value, '388170e32dc0ba9b864085b38e0e6442')

    def testTc2(self):
        """Invalid case in which all the information is correct but the person
        already has a reservation"""

        myManager = hotelManager()
        info = (5555555555554444, "Santiago P", 100, 100000000, "single",
                "2024-01-01", 1)
        # TC2
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), info[1] + " already has a reservation")

class testGuestArrival(unittest.TestCase):
    """Test cases for the second function"""
    @freeze_time('2024-01-01')
    def testTc1Valid(self):
        """Valid case in which all the information is correct"""

        myManager = hotelManager()
        filepath = "JSONtestsFunction2/TC1Valid.json"
        # TC1Valid.json
        value = myManager.guestArrival(filepath)
        self.assertEqual(value, '3b1d74eb423528c1f948a13a01ee880589ca0c2c489c5d1fa6b06fb0b1c527b3')

    def testTc2(self):
        """Test for the second case, empty file"""
        # JSON empty file name
        myManager = hotelManager()
        filePath = "JSONtestsFunction2/TC2.json"
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
        filePath = "JSONtestsFunction2/TC3.json"
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
        filePath = "JSONtestsFunction2/TC4.json"
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
        filePath = "JSONtestsFunction2/TC5.json"
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
        filePath = "JSONtestsFunction2/TC6.json"  # Use the file test.json
        value = myManager.guestArrival(filePath)
        self.assertEqual(value,
                         '3b1d74eb423528c1f948a13a01ee880589ca0c2c489c5d1fa6b06fb0b1c527b3')
    def testTc7F1DEL(self):
        """Test for the seventh case, one of the fields is deleted. In this
        case only F1."""

        fileName = "JSONtestsFunction2/TC7F1.json"  # JSON empty file name
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
        fileName = "JSONtestsFunction2/TC7F2.json"
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
        fileName = "JSONtestsFunction2/TC8.json"
        myManager = hotelManager()
        value = myManager.guestArrival(fileName)
        self.assertEqual(value, '3b1d74eb423528c1f948a13a01ee880589ca0c2c489c5d1fa6b06fb0b1c527b3')

    def testTc9MOD(self):
        """Test for the ninth case, separator is modified"""

        # JSON file name
        fileName = "JSONtestsFunction2/TC9.json"
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
        fileName = "JSONtestsFunction2/TC9.json"

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
        """Test for the tenth case, data1 or value1 duplicated or deleted. We
        only need to test one of the cases (data1 or value1 / DEL OR DUP)"""

        # JSON file name
        fileName = "JSONtestsFunction2/TC10.json"

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
        fileName = "JSONtestsFunction2/TC11.json"

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
        fileName = "JSONtestsFunction2/TC12.json"

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
        fileName = "JSONtestsFunction2/TC12.json"

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
        fileName = "JSONtestsFunction2/TC13.json"

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
        fileName = "JSONtestsFunction2/TC14.json"

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
        fileName = "JSONtestsFunction2/TC15.json"

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
        fileName = "JSONtestsFunction2/TC16.json"

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
        filename = "JSONtestsFunction2/TC17.json"

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
