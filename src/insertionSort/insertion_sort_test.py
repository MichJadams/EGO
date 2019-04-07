import unittest
import insertion_sort

class insertion_sort_test(unittest):
    def setUp(self):
        try:
            self.testClass = insertion_sort.insertionSort()
        except NameError as e:
            pass
if __name__ == '__main__':
    unittest.main()
