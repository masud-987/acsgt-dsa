from typing import List

class BubbleSort:
    def __init__(self, arr: List[int] ) -> None:
        self.arr = arr
    
    def b_search(self) -> List[int]:
        """
        performs bubble sort on a given array.
        after sorting the array, It returns the sorted array.

        """
        sorted = False
        unsorted_index = len(self.arr) - 1
        
        while not sorted:
            sorted = True
            for i in range(unsorted_index):
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    sorted = False
            unsorted_index -= 1 ## Removing the last element from array out of next itteration.
        return self.arr
    
li = BubbleSort([1,3,4,8,7,98,99,41,20])
print(li.b_search())