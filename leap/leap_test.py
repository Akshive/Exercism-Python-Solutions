import unittest

from leap import leap_year

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.5.1


class LeapTest(unittest.TestCase):
    def test_year_not_divisible_by_4_in_common_year(self):
        self.assertIs(leap_year(2015), False)

    def test_year_divisible_by_2_not_divisible_by_4_in_common_year(self):
        self.assertIs(leap_year(1970), False)

    def test_year_divisible_by_4_not_divisible_by_100_in_leap_year(self):
        self.assertIs(leap_year(1996), True)

    def test_year_divisible_by_100_not_divisible_by_400_in_common_year(self):
        self.assertIs(leap_year(2100), False)

    def test_year_divisible_by_400_in_leap_year(self):
        self.assertIs(leap_year(2000), True)

    def test_year_divisible_by_200_not_divisible_by_400_in_common_year(self):
        self.assertIs(leap_year(1800), False)


if __name__ == "__main__":
    unittest.main()
