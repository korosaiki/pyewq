import unittest
from count import Count
import time
class countt(unittest.TestCase):
    def setUp(self):
        print ("测试通过")
        time.sleep(3)
    def tearDown(self):
        print("测试不通过")
        time.sleep(3)
    def test__add(self):
        J = Count(3,4)
        ADD = J.add()
        self.assertEqual(ADD,7)
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite
    suite.addTest(countt("test_add()"))
    runner = unittest.TextTestRunner
    runner.run(countt("test_add"))