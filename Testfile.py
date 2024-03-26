"""File with all the tests of each function"""
import json
import unittest
from UC3MTravel import hotelManagementException
from UC3MTravel.HotelManager import HotelManager

class testGuestArrival(unittest.TestCase):
    """Test cases for the second function"""

    def testTc1Valid(self):
        """Valid case in which all the information is correct"""
        # Data for the test
        testData = {
            "Localizer": "d32ff67ec38aab9dda77c20b4aef2762",
            "IdCard": 1236
        }
        testList = [testData]
        # JSON name
        fileName = "test.json"

        # Write data in json file
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile)

        myManager = HotelManager()
        filePath = "test.json"  # Use the file test.json
        value = myManager.guest_arrival(filePath)
        self.assertEqual(value, '256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6')

    def testTc2(self):
        """Test for the second case, empty file"""
        # JSON empty file name
        myManager = HotelManager()
        filePath = "emptyforTC2.json"
        exception = None
        try:
            myManager.guest_arrival(filePath)
        except hotelManagementException as e:
            exception = e

        # Verify if there was an exception and if the correct message was
        # displayed
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")


if __name__ == '__main__':
    unittest.main()
