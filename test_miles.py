import miles
import sqlite3
import unittest
from unittest import TestCase

class TestMileageDB(TestCase):

    test_db_url = 'test_miles.db'

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        # Overwrite the mileage
        miles.db_url = self.test_db_url
        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('DELETE FROM miles')
        conn.commit()
        conn.close()

    def test_add_new_vehicle(self):
        miles.add_miles('Blue Car', 100)
        expected = { 'Blue Car': 100 }
        self.compare_db_to_expected(expected)

        miles.add_miles('Green Car', 50)
        expected['Green Car'] = 50
        self.compare_db_to_expected(expected)

    def test_increase_miles_for_vehicle(self):
        miles.add_miles('Red Car', 100)
        expected = { 'Red Car': 100 }
        self.compare_db_to_expected(expected)

        miles.add_miles('Red Car', 50)
        expected['Red Car'] = 100 + 50
        self.compare_db_to_expected(expected)

    def test_add_new_vehicle_no_vehicle(self):
        with self.assertRaises(Exception):
            mileage.addMiles(None, 100)

    def test_miles_upper_case(self):
        v1 = miles_upper_case('yellow car')
        mileage.add_miles(v1, 200)
        expected = 'YELLOW CAR'
        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM MILES').fetchall()

        for row in all_data:
            # Vehicle exists, and mileage is correct
            self.assertEqual(row[0], expected)
            # self.assertEqual(expected[row[0]], row[1])

    def test_add_new_vehicle_invalid_new_miles(self):
        with self.assertRaises(Exception):
            mileage.addMiles('Car', -100)
        with self.assertRaises(Exception):
            mileage.addMiles('Car', 'abc')
        with self.assertRaises(Exception):
            mileage.addMiles('Car', '12.def')

    # This is not a test method, instead, it's used by the test methods
    def compare_db_to_expected(self, expected):

        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM MILES').fetchall()

        # Same rows in DB as entries in expected dictionary
        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            # Vehicle exists, and mileage is correct
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])

        conn.close()


class TestMileageDB_1(TestCase):

    test_db_url = 'test_miles.db'

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        # Overwrite the mileage
        miles.db_url = self.test_db_url
        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('DELETE FROM miles')
        conn.commit()
        conn.close()

    def test_search(self):
        v1 = miles_upper_case('white car')
        mileage.add_miles(v1, 200)
        search_vehicle =  mileage.search_vehicle(v1)


        self.assertIsNotNone(search_vehicle)


if __name__ == '__main__':
     unittest.main()
