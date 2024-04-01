import unittest
from pathlib import Path
from freezegun import freeze_time
from UC3MTravel.HotelManagementException import hotelManagementException
from UC3MTravel.HotelManager import hotelManager


class TestGuestCheckout(unittest.TestCase):
    """Test cases for the third function"""
    @freeze_time('2024-01-01')
    def testTc1Valid(self):
        """Valid case in which the key and the departure date are correct"""
        myManager = hotelManager()
        try:
            info = (
            5555555555554444, "Barbara Sanchez", 456, 123456788, "single",
            "2024-01-01", 1)
            myManager.roomReservation(*info)
        except hotelManagementException:
            """Reservation already done"""
            ...

        filePath = (
                    str(Path.home()) + "\G88.2024.T05.GE2\src\JSONfiles\JsonForTests\TC_3_1.json")
        key = myManager.guestArrival(filePath)

        result = myManager.guestCheckout(key)
        self.assertEqual(result, True)


    def testTc3_2(self):
        """Invalid case in which the key is less than 64 bytes long."""

        myManager = hotelManager()
        key = "6A503F9B"
        exception = None
        try:
            myManager.guestCheckout(key)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Not processable room code.")

    def testTc3_3(self):
        """Invalid case in which the key is more than 64 bytes long."""

        myManager = hotelManager()
        key = "394A77354C6D52633767585A386551733256705974365542783344664776314B6F34546245694168576E5A7946313055714D685064533443"
        exception = None
        try:
            myManager.guestCheckout(key)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Not processable room code.")

    def testTc3_4(self):
        """Invalid case in which the key is not in hexadecimal."""

        myManager = hotelManager()
        key = "key7Gj45K3z1RlPv92tZx0q9sD8LE6h5fB4nJKXeVWcOmaTugMYIdUiFpQboHrN"
        exception = None
        try:
            myManager.guestCheckout(key)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Not processable room code.")

    def testTc3_5(self):
        """Invalid case in which the key is valid but not registered."""

        myManager = hotelManager()
        key = "1c8ffb7df9f4a520ad0353d10386b0b921c353ee16b9e4b9e2af56da4ed1d596"
        exception = None
        try:
            myManager.guestCheckout(key)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Such key is not registered.")

    @freeze_time('2024-01-01')
    def testTc3_6(self):
        """Invalid case in which the key is valid but the departure date is not."""

        myManager = hotelManager()
        try:
            info = (5555555555554444, "Robert DeNiro", 789, 987654321, "suite", "2024-01-01", 3)
            myManager.roomReservation(*info)
        except hotelManagementException:
            """Reservation already done"""
            ...

        filePath = (str(Path.home()) + "\G88.2024.T05.GE2\src\JSONfiles\JsonForTests\TC_3_2.json")
        key = myManager.guestArrival(filePath)
        exception = None
        try:
            myManager.guestCheckout(key)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "Departure date is not valid.")