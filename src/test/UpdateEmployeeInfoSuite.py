import unittest
from TestUtils import TestUpdateEmployeeInfo


class UpdateEmployeeInfoSuite(unittest.TestCase):
    def test_1(self):
        """Update name"""
        name = "Cao Trung"
        gender = ""
        birth = ""
        address = ""
        expect = "Update successfully"
        self.assertTrue(TestUpdateEmployeeInfo.test(name, gender, birth, address, expect, 201))

    def test_2(self):
        """Update gender"""
        name = ""
        gender = "Nữ"
        birth = ""
        address = ""
        expect = "Update successfully"
        self.assertTrue(TestUpdateEmployeeInfo.test(name, gender, birth, address, expect, 202))

    def test_3(self):
        """Update birthday"""
        name = ""
        gender = ""
        birth = "11/11/2002"
        address = ""
        expect = "Update successfully"
        self.assertTrue(TestUpdateEmployeeInfo.test(name, gender, birth, address, expect, 203))

    def test_4(self):
        """Update address"""
        name = ""
        gender = ""
        birth = ""
        address = "Quảng Nam"
        expect = "Update successfully"
        self.assertTrue(TestUpdateEmployeeInfo.test(name, gender, birth, address, expect, 204))

    def test_5(self):
        """Update with an empty name value"""
        name = "empty"
        gender = ""
        birth = ""
        address = ""
        expect = "Failed"
        self.assertTrue(TestUpdateEmployeeInfo.test(name, gender, birth, address, expect, 205))

    def test_6(self):
        """Update with an empty gender value"""
        name = ""
        gender = "empty"
        birth = ""
        address = ""
        expect = "Failed"
        self.assertTrue(TestUpdateEmployeeInfo.test(name, gender, birth, address, expect, 206))

    def test_7(self):
        """Update with an empty address"""
        name = ""
        gender = ""
        birth = ""
        address = "empty"
        expect = "Failed"
        self.assertTrue(TestUpdateEmployeeInfo.test(name, gender, birth, address, expect, 207))