import unittest
from TestUtils import TestCreateLeaveRequest


class CreateLeaveRequestSuite(unittest.TestCase):
    def test_1(self):
        """Create full filled leave request"""
        start_date = "2023-12-05"
        end_date = "2023-12-09"
        reason = "test1-reason"
        expect = "Successfully Create A Request"
        self.assertTrue(TestCreateLeaveRequest.test(start_date, end_date, reason, expect, 101))
    
    def test_2(self):
        """Create leave request ONLY with START_DATE and END_DATE"""
        start_date = "2023-12-05"
        end_date = "2023-12-09"
        reason = ""
        expect = "Failed"
        self.assertTrue(TestCreateLeaveRequest.test(start_date, end_date, reason, expect, 102))
    
    def test_3(self):
        """Create leave request only with START_DATE"""
        start_date = "2023-12-05"
        end_date = ""
        reason = ""
        expect = "Failed"
        self.assertTrue(TestCreateLeaveRequest.test(start_date, end_date, reason, expect, 103))
    
    def test_4(self):
        """Create leave request only with END_DATE"""
        start_date = ""
        end_date = "2023-12-09"
        reason = ""
        expect = "Failed"
        self.assertTrue(TestCreateLeaveRequest.test(start_date, end_date, reason, expect, 104))
    
    def test_5(self):
        """Create leave request ONLY with REASON"""
        start_date = ""
        end_date = ""
        reason = "a reason to absence"
        expect = "Failed"
        self.assertTrue(TestCreateLeaveRequest.test(start_date, end_date, reason, expect, 105))
    
    def test_6(self):
        """Create Empty leave request"""
        start_date = ""
        end_date = ""
        reason = ""
        expect = "Failed"
        self.assertTrue(TestCreateLeaveRequest.test(start_date, end_date, reason, expect, 106))