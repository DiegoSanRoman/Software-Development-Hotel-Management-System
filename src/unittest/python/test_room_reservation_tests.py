import unittest
from UC3MTravel.HotelManagementException import hotelManagementException
from UC3MTravel.HotelManager import hotelManager
import json
from pathlib import Path


class TestRoomReservation(unittest.TestCase):
    """Test cases for the first function"""

    def testTc1Valid(self):
        """Valid case in which all the information is correct and the person
        does not already have a reservation"""

        myManager = hotelManager()
        info = (5555555555554444, "Santiago P", 100, 100000000, "single",
                "2024-01-01", 1)
        # TC1Valid
        value = myManager.roomReservation(*info)
        self.assertEqual(value, 'c2ed8a2592353c525477b7c33771fc4f')

        # Cleanup: Remove the information from Reservations.json
        reservation_file = str(
            Path.home()) + "/G88.2024.T05.GE2/src/JSONfiles/JsonForFunctions/Reservations.json"
        try:
            with open(reservation_file, 'r+') as f:
                reservations = json.load(f)

                # Remove both reservations (if they exist)
                if reservations:
                    reservations.pop()

                f.seek(0)  # Move the file pointer to the beginning
                json.dump(reservations, f, indent=4)
                f.truncate()  # Remove any remaining content beyond the new JSON data
        except FileNotFoundError:
            pass

    def testTc2(self):
        """Invalid case in which all the information is correct but the person
        already has a reservation"""

        myManager = hotelManager()
        info = (5555555555554444, "Santiago P", 100, 100000000, "single",
                "2024-01-01", 1)

        # First attempt to introduce the reservation (We expect no output,
        # just for the reservation to be succesfully introduced in the file)
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            self.fail("First attempt to reserve a room failed unexpectedly: {}".format(e))

        # Second attempt to introduce the same reservation (We expect an exception)
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # Verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception),
                         info[1] + " already has a reservation")

        # Cleanup: Remove the information from Reservations.json
        reservation_file = str(
            Path.home()) + "/G88.2024.T05.GE2/src/JSONfiles/JsonForFunctions/Reservations.json"
        try:
            with open(reservation_file, 'r+') as f:
                reservations = json.load(f)

                # Remove both reservations (if they exist)
                if reservations:
                    reservations.pop()


                f.seek(0)  # Move the file pointer to the beginning
                json.dump(reservations, f, indent=4)
                f.truncate()  # Remove any remaining content beyond the new JSON data
        except FileNotFoundError:
            pass

    def testTc3(self):
        """Invalid case in which the credit card number is not of the
        correct datatype"""

        myManager = hotelManager()
        info = ("credit_card_number", "Santiago P", 100, 100000000, "single",
                "2024-01-01", 1)
        # TC3
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
                "2024-01-01", 1)
        # TC4
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
                "2024-01-01", 1)
        # TC5
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
                "2024-01-01", 1)
        # TC6
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
                "2024-01-01", 1)
        # TC7
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
                "2024-01-01", 1)
        # TC8
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
        info = (5555555555554444, "Dulceidainfluencer", 100, 100000000,
                "single",
                "2024-01-01", 1)
        # TC9
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
                "2024-01-01", 1)
        # TC10
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
                "2024-01-01", 1)
        # TC11
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
                "2024-01-01", 1)
        # TC12
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid ID card (3 digits needed)")

    def testTc13(self):
        """Invalid case in which the id card has 4 digits (instead of 3)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 7777, 100000000, "single",
                "2024-01-01", 1)
        # TC13
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid ID card (3 digits needed)")

    def testTc14(self):
        """Invalid case in which the id card has only two digits (instead of
        3)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 33, 100000000, "single",
                "2024-01-01", 1)
        # TC14
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid ID card (3 digits needed)")

    def testTc15(self):
        """Invalid case in which the phone number is of the incorrect datatype"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, "phonenumber",
                "single", "2024-01-01", 1)
        # TC15
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
                "single", "2024-01-01", 1)
        # TC16
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
                "single", "2024-01-01", 1)
        # TC17
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
                45, "2024-01-01", 1)
        # TC18
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
                "premium", "2024-01-01", 1)
        # TC19
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid room type")

    def testTc20(self):
        """Invalid case in which the arrival date is of the incorrect
        datatype"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", 56, 1)
        # TC20
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid arrival date format")

    def testTc21(self):
        """Invalid case in which the arrival date is a string but it is too
        long (more than 10 characters)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "icandoeverything", 1)
        # TC21
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid arrival date format")

    def testTc22(self):
        """Invalid case in which the arrival date is a string but it is too
        short (less than 10 characters)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "oops", 1)
        # TC22
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid arrival date format")

    def testTc23(self):
        """Invalid case in which the arrival date is a string and has the
        correct length (10 characters), but the format is not the correct
        one  (DD/MM/YYYY)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "0103--2024", 1)
        # TC23
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid arrival date format")

    def testTc24(self):
        """Invalid case in which the arrival date is a string, has the
        correct length (10 characters) and the correct format (DD/MM/YYYY),
        but the day is not one of the accepted values (01-31)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "2024-11-00", 1)
        # TC24
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid day in arrival date")

    def testTc25(self):
        """Invalid case in which the arrival date is a string, has the
        correct length (10 characters) and the correct format (DD/MM/YYYY),
        but the day is not one of the accepted values (01-31)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "2024-11-32", 1)
        # TC25
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid day in arrival date")

    def testTc26(self):
        """Invalid case in which the arrival date is a string, has the
        correct length (10 characters) and the correct format (DD/MM/YYYY),
        but the month is not one of the accepted values (01-12)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "2024-00-11", 1)
        # TC26
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid month in arrival date")

    def testTc27(self):
        """Invalid case in which the arrival date is a string, has the
        correct length (10 characters) and the correct format (DD/MM/YYYY),
        but the month is not one of the accepted values (01-12)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "2024-13-11", 1)
        # TC27
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid month in arrival date")

    def testTc28(self):
        """Invalid case in which the arrival date is a string, has the
        correct length (10 characters) and the correct format (DD/MM/YYYY),
        but the year is not one of the accepted values (current year-9999)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "2023-11-11", 1)
        # TC28
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid year in arrival date")

    def testTc29(self):
        """Invalid case in which the arrival date is a string, has the
        correct length (10 characters) and the correct format (DD/MM/YYYY),
        but the year is not one of the accepted values (current year-9999)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "10000-11-11", 1)
        # TC29
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid arrival date format")

    def testTc30(self):
        """Invalid case in which the number of days is not of the correct
        datatype"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "2031-11-11", "nini")
        # TC30
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid number of days")

    def testTc31(self):
        """Invalid case in which the number of days is not one of the
        accepted values (1-10)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "2031-11-11", 0)
        # TC31
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid number of days")

    def testTc32(self):
        """Invalid case in which the number of days is not one of the
        accepted values (1-10)"""

        myManager = hotelManager()
        info = (5555555555554444, "Belen Izantina", 100, 123456789,
                "single", "2031-11-11", 11)
        # TC32
        exception = None
        try:
            myManager.roomReservation(*info)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Invalid number of days")

if __name__ == '__main__':
    unittest.main()