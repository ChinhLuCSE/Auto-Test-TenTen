import unittest
from selenium.common.exceptions import NoSuchElementException
from TestUtils_ThinhTo import TestStatistic
import time


class MyTestCase(unittest.TestCase):
    def test_1_statis_only(self):
        approved = 0
        status_month = "1"
        dayoff_month = "1"
        start_date = "2023-12-01"
        end_date = "2023-12-01"
        expected_status = 1
        expected_dayoff = 0
        self.assertEqual(
            TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
                                   expected_dayoff, True), (True, True))

    def test_2_statis_only(self):
        approved = 0
        status_month = "3"
        dayoff_month = "1"
        start_date = "2023-12-01"
        end_date = "2023-12-01"
        expected_status = 1
        expected_dayoff = 0
        self.assertEqual(
            TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
                                   expected_dayoff, True), (True, True))

    def test_3_statis_only(self):
        approved = 0
        status_month = "1"
        dayoff_month = "3"
        start_date = "2023-12-01"
        end_date = "2023-12-01"
        expected_status = 1
        expected_dayoff = 0
        self.assertEqual(
            TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
                                   expected_dayoff, True), (True, True))

    def test_4_statis_only(self):
        approved = 0
        status_month = "3"
        dayoff_month = "3"
        start_date = "2023-12-01"
        end_date = "2023-12-01"
        expected_status = 1
        expected_dayoff = 0
        self.assertEqual(
            TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
                                   expected_dayoff, True), (True, True))

    # def test_1(self):
    #     approved = 0
    #     status_month = "1"
    #     dayoff_month = "1"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_2(self):
    #     approved = 0
    #     status_month = "3"
    #     dayoff_month = "1"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_3(self):
    #     approved = 0
    #     status_month = "1"
    #     dayoff_month = "3"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_4(self):
    #     approved = 0
    #     status_month = "3"
    #     dayoff_month = "3"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_5(self):
    #     approved = 0
    #     status_month = "1"
    #     dayoff_month = "1"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-03"
    #     expected_status = 0
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_6(self):
    #     approved = 0
    #     status_month = "3"
    #     dayoff_month = "1"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-03"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_7(self):
    #     approved = 0
    #     status_month = "1"
    #     dayoff_month = "3"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-03"
    #     expected_status = 0
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_8(self):
    #     approved = 0
    #     status_month = "3"
    #     dayoff_month = "3"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-03"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_9(self):
    #     approved = 1
    #     status_month = "1"
    #     dayoff_month = "1"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 1
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_10(self):
    #     approved = 1
    #     status_month = "3"
    #     dayoff_month = "1"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 1
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_11(self):
    #     approved = 1
    #     status_month = "1"
    #     dayoff_month = "3"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 1
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_12(self):
    #     approved = 1
    #     status_month = "3"
    #     dayoff_month = "3"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 1
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_13(self):
    #     approved = 1
    #     status_month = "1"
    #     dayoff_month = "1"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-01"
    #     expected_status = 0
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_14(self):
    #     approved = 1
    #     status_month = "3"
    #     dayoff_month = "1"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-01"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_15(self):
    #     approved = 1
    #     status_month = "1"
    #     dayoff_month = "3"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-01"
    #     expected_status = 0
    #     expected_dayoff = 1
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_16(self):
    #     approved = 1
    #     status_month = "3"
    #     dayoff_month = "3"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-01"
    #     expected_status = 1
    #     expected_dayoff = 1
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_17(self):
    #     approved = 2
    #     status_month = "1"
    #     dayoff_month = "1"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_18(self):
    #     approved = 2
    #     status_month = "3"
    #     dayoff_month = "1"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_19(self):
    #     approved = 2
    #     status_month = "1"
    #     dayoff_month = "3"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_20(self):
    #     approved = 2
    #     status_month = "3"
    #     dayoff_month = "3"
    #     start_date = "2023-12-01"
    #     end_date = "2023-12-01"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_21(self):
    #     approved = 2
    #     status_month = "1"
    #     dayoff_month = "1"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-03"
    #     expected_status = 0
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_22(self):
    #     approved = 2
    #     status_month = "3"
    #     dayoff_month = "1"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-03"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_23(self):
    #     approved = 2
    #     status_month = "1"
    #     dayoff_month = "3"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-03"
    #     expected_status = 0
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))
    #
    # def test_24(self):
    #     approved = 2
    #     status_month = "3"
    #     dayoff_month = "3"
    #     start_date = "2023-11-01"
    #     end_date = "2023-11-03"
    #     expected_status = 1
    #     expected_dayoff = 0
    #     self.assertEqual(
    #         TestStatistic.mainFlow(approved, status_month, dayoff_month, start_date, end_date, expected_status,
    #                                expected_dayoff), (True, True))


if __name__ == '__main__':
    unittest.main()
