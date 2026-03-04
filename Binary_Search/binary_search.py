from typing import List

class BinarySearch:
    def __init__(self, arr: List[int], x: int) -> None:
        self.array = arr
        self.x     = x
    
    def search(self) -> int:
        """
        perform the binary search on array to find x item,
        if found return the index otherwise return -1
        """
        low , high= 0, len(self.array) - 1

        while low <= high:
            mid = (high+low) // 2
            if self.x == self.array[mid]:
                return mid
            elif self.array[mid] < self.x:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    

x = BinarySearch([2,34,45,55,56,89,90,100],99)
print(x.search())