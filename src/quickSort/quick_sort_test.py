import unittest
import quick_sort

class quick_sort_test(unittest.TestCase):
    def setUp(self):
        try:
            self.assertTrue(os.path.isfile('./quick_sort_test.py'))
            self.testClass = quick_sort.quickSorter()
        except NameError as e:
            self.fail()
