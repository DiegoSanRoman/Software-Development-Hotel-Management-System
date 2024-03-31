import unittest
from freezegun import freeze_time
from src.main.python.UC3MTravel.HotelManagementException import hotelManagementException
from src.main.python.UC3MTravel.HotelManager import hotelManager

class TestGuestCheckout(unittest.TestCase):
    """Test cases for the third function"""
    @freeze_time('2024-01-01')
    def testTc1Valid(self):
        """Valid case in which the key, the departure date and the 2 json files are correct"""

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