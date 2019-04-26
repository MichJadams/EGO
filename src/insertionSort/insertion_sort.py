class insertion_sorter:
    def __init__(self, array):
        self.arrayToSort = array
        self.sortedStates = []

    def insertionSort(self):
        for index, value in enumerate(self.arrayToSort):
            self.insert(self.arrayToSort, index, value)
            self.sortedStates.append(self.arrayToSort.copy())
        return self.arrayToSort

    def insert(self,array,index, value):
        index -= 1
        while index >= 0 and array[index] > value:
            array[index + 1] = array[index]
            index -= 1

        array[index + 1] = value
