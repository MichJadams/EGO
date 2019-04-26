import unittest
import insertion_sort

class insertion_sort_test(unittest.TestCase):
    def setUp(self):
        try:
            self.testClass = insertion_sort.insertion_sorter([])
        except NameError as e:
            pass

    def test_returns_empty_array(self):
        self.testClass = insertion_sort.insertion_sorter([])
        result = self.testClass.insertionSort()
        failMsg = "insertionSort does not return an empty array when passed one"
        self.assertEqual(0, len(result), failMsg)

    def test_sorts_small_array(self):
        self.testClass = insertion_sort.insertion_sorter([1,5,4])
        result = self.testClass.insertionSort()
        expected = [1,4,5]
        for index in range(0,len(result)):
            failMsg = "incorrect value at {0}".format(index)
            self.assertEqual(expected[index],result[index], failMsg)

    def test_stores_correct_intermediate_sorted_states(self):
        self.testClass = insertion_sort.insertion_sorter([1,4,3,2,7,5,6,9])
        result = self.testClass.insertionSort()
        actualIntermediatStates = self.testClass.sortedStates
        expectedIntermediateStates = [[1,4,3,2,7,5,6,9],[1,4,3,2,7,5,6,9],
        [1,3,4,2,7,5,6,9],[1,2,3,4,7,5,6,9],[1,2,3,4,7,5,6,9],[1,2,3,4,5,7,6,9],[1,2,3,4,5,6,7,9],[1,2,3,4,5,6,7,9]]
        self.assertEqual(len(expectedIntermediateStates), len(actualIntermediatStates),
        msg="The expected and the actual intermediate states are of different lengths")
        
        for arrayIndex in range(0, len(expectedIntermediateStates)):
            for numberIndex in range(0, len(expectedIntermediateStates)):
                self.assertEqual(expectedIntermediateStates[arrayIndex][numberIndex],actualIntermediatStates[arrayIndex][numberIndex])

if __name__ == '__main__':
    unittest.main()
