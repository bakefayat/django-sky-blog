import unittest
from datetime import date
from extensions.jalali import Gregorian, Persian


class TestGregorian(unittest.TestCase):
    def test_init_str(self):
        g = Gregorian("2023-04-09")
        self.assertEqual(g.persian_tuple(), (1402, 1, 20))

    def test_init_date(self):
        d = date(2023, 4, 9)
        g = Gregorian(d)
        self.assertEqual(g.persian_tuple(), (1402, 1, 20))

    def test_init_tuple(self):
        g = Gregorian(2023, 4, 9)
        self.assertEqual(g.persian_tuple(), (1402, 1, 20))

    def test_init_invalid_input(self):
        with self.assertRaises(Exception):
            Gregorian("invalid")
        with self.assertRaises(Exception):
            Gregorian(2023, 4, 31)

    def test_persian_string(self):
        g = Gregorian("2023-04-09")
        self.assertEqual(g.persian_string(), "1402-1-20")
        self.assertEqual(g.persian_string("{}/{}/{}"), "1402/1/20")


if __name__ == "__main__":
    unittest.main()
