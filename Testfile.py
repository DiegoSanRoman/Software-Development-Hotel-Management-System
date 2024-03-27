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
        filePath = "JSONtestsFunction2/emptyforTC2.json"
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
        # Data for the test
        testData = {
        }
        testList = [testData]
        # JSON name
        fileName = "test.json"

        # Write data in json file
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile)
        # JSON empty file name
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
    def testTc6(self):
        """Test for the sixth case, duplicated data"""
        # Data for the test
        testData = {
            "Localizer": "d32ff67ec38aab9dda77c20b4aef2762",
            "IdCard": 1236,
            "Localizer": "d32ff67ec38aab9dda77c20b4aef2762",
            "IdCard": 1236
        }
        testList = [testData]
        # JSON name
        fileName = "test.json"

        # Write data in json file
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile)
        # JSON empty file name
        myManager = HotelManager()
        value = myManager.guest_arrival(fileName)
        self.assertEqual(value, '256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6')
    def testTc7F1DEL(self):
        """Test for the seventh case, one of the fields del or dup"""
        # Data for the test
        testData = {
            "IdCard": 1236
        }
        testList = [testData]
        # JSON name
        fileName = "test.json"

        # Write data in json file
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile)
        # JSON empty file name
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
        """Test for the seventh case, one of the fields del or dup"""
        # Data for the test
        testData = {
            "Localizer": "d32ff67ec38aab9dda77c20b4aef2762"
        }
        testList = [testData]
        # JSON name
        fileName = "test.json"

        # Write data in json file
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile)
        # JSON empty file name
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
        """Test for the seventh case, one of the fields del or dup"""
        # Data for the test
        testData = {
            "Localizer": "d32ff67ec38aab9dda77c20b4aef2762",
            "Localizer": "d32ff67ec38aab9dda77c20b4aef2762",
            "IdCard": 1236
        }
        testList = [testData]
        # JSON name
        fileName = "test.json"

        # Write data in json file
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile)
        # JSON empty file name
        myManager = HotelManager()
        value = myManager.guest_arrival(fileName)
        self.assertEqual(value, '256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6')
    def testTc8F2DEL(self):
        """Test for the seventh case, one of the fields del or dup"""
        # Data for the test
        testData = {
            "Localizer": "d32ff67ec38aab9dda77c20b4aef2762",
            "IdCard": 1236,
            "IdCard": 1236
        }
        testList = [testData]
        # JSON name
        fileName = "test.json"

        # Write data in json file
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile)
        # JSON empty file name
        myManager = HotelManager()
        value = myManager.guest_arrival(fileName)
        self.assertEqual(value, '256a59af85d250a299da5d62bb797f7a1a1ef1007737f6b1dcc2d48114c21ac6')

    def testTc9MOD(self):
        """Test for the ninth case, separator is modified"""
        # Datos para el test con separador modificado
        testData = {
            "Localizer": "d32ff67ec38aab9dda77c20b4aef2762",
            "IdCard": 1236
        }
        testList = [testData]

        # JSON file name
        fileName = "test.json"

        # write data in JSON with modified separator
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile, separators=(';', ':'))

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
        # Datos para el test con separador modificado
        testData = {
            "Localizer": "d32ff67ec38aab9dda77c20b4aef2762",
            "IdCard": 1236
        }
        testList = [testData]

        # JSON file name
        fileName = "test.json"

        # write data in JSON with modified separator
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile, separators=(',,', ';;'))

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
        """Test for the tenth case, data1 or value1 duplicated. We only need
        to test one of the cases (data1 or value1)"""
        # Datos para el test con separador modificado
        testData = {
            "Localizer""Localizer": "d32ff67ec38aab9dda77c20b4aef2762",
            "IdCard": 1236
        }
        testList = [testData]

        # JSON file name
        fileName = "test.json"

        # write data in JSON with modified separator
        with open(fileName, "w", encoding='utf-8') as jsonFile:
            json.dump(testList, jsonFile, separators=(',,', ';;'))

        myManager = HotelManager()
        exception = None
        try:
            myManager.guest_arrival(fileName)
        except hotelManagementException as e:
            exception = e

        # verify exception
        self.assertIsNotNone(exception)
        self.assertEqual(str(exception), "File not found or empty file")
if __name__ == '__main__':
    unittest.main()
