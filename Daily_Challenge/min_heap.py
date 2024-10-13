class MinHeap():
    def __init__(self, values):
        self.heap = []
        self.itemCount = 0
        for value in values:
            self.insert(value)
    
    def __repr__(self):
        return str(self.heap)
    
    def insert(self, value):
        # return the total items now, i guess
        if value != None:
            self.heap.append(value)
        else:
            raise ValueError("Tried to insert None...")
        self.itemCount += 1
        self._bubble_up()
        return self.itemCount
    
    def _bubble_up(self): # iterative
        bubble = self.itemCount - 1
        parent = ( bubble - 1 ) // 2
        while bubble != 0 and self.heap[bubble] < self.heap[parent]:
            self.heap[parent], self.heap[bubble] = self.heap[bubble], self.heap[parent]
            bubble = parent
            parent = ( bubble - 1 ) // 2
    
    def pop(self):
        if not self.heap:
            raise IndexError("pop attempted on empty heap")
        returnVal = self.heap[0]
        self.heap[0], self.heap[self.itemCount - 1] = self.heap[self.itemCount - 1], self.heap[0]
        self.heap = self.heap[:-1]
        self.itemCount -= 1
        if self.heap: # don't bubble if heap is empty
            self._bubble_down(0)
        return returnVal
    
    def _bubble_down(self, index): # recursive
        child1 = 2 * index + 1 if 2 * index + 1 < self.itemCount else None
        child2 = 2 * index + 2 if 2 * index + 2 < self.itemCount else None
        swapChild = child1 if child1 and self.heap[child1] < self.heap[index] else None
        swapChild = child2 if child2 and self.heap[child2] < self.heap[index] and self.heap[child2] < self.heap[child1] else swapChild
        if swapChild:
            # swap
            self.heap[index], self.heap[swapChild] = self.heap[swapChild], self.heap[index]
            self._bubble_down(swapChild)
        # finished
        return
    
def test_heap():
    # Test case 1: Basic insertions
    heap = MinHeap([10, 5, 20, 3, 15])
    assert heap.heap == [3, 5, 20, 10, 15], f"Test Case 1 Failed: Expected [3, 5, 20, 10, 15], but got {heap.heap}"

    # Test case 2: Popping the smallest element (multiple pops)
    assert heap.pop() == 3, f"Test Case 2 Failed: Expected 3, but got {heap.pop()}"
    assert heap.pop() == 5, f"Test Case 2 Failed: Expected 5, but got {heap.pop()}"
    assert heap.heap == [10, 15, 20], f"Test Case 2 Failed: Expected [10, 15, 20], but got {heap.heap}"

    # Test case 3: Inserting into the heap after pops
    heap.insert(1)
    assert heap.heap == [1, 10, 20, 15], f"Test Case 3 Failed: Expected [1, 10, 20, 15], but got {heap.heap}"

    # Test case 4: Handling duplicates
    heap.insert(15)
    assert heap.heap == [1, 10, 20, 15, 15], f"Test Case 4 Failed: Expected [1, 10, 20, 15, 15], but got {heap.heap}"
    
    # Pop elements and check the heap structure
    assert heap.pop() == 1, f"Test Case 4 Failed: Expected 1, but got {heap.pop()}"
    assert heap.heap == [10, 15, 20, 15], f"Test Case 4 Failed: Expected [10, 15, 20, 15], but got {heap.heap}"

    # Test case 5: Inserting negative numbers
    heap = MinHeap([-10, -5, -20, 0, 5])
    assert heap.heap == [-20, -5, -10, 0, 5], f"Test Case 5 Failed: Expected [-20, -5, -10, 0, 5], but got {heap.heap}"

    # Pop elements and check the heap structure
    assert heap.pop() == -20, f"Test Case 5 Failed: Expected -20, but got {heap.pop()}"
    assert heap.pop() == -10, f"Test Case 5 Failed: Expected -10, but got {heap.pop()}"
    assert heap.heap == [-5, 0, 5], f"Test Case 5 Failed: Expected [-5, 5, 0], but got {heap.heap}"

    # Test case 6: Edge case of popping from a heap with one element
    heap = MinHeap([100])
    assert heap.pop() == 100, f"Test Case 6 Failed: Expected 100, but got {heap.pop()}"
    assert heap.heap == [], f"Test Case 6 Failed: Expected [], but got {heap.heap}"

    # Test case 7: Pop from empty heap (should raise IndexError)
    try:
        heap.pop()
        assert False, "Test Case 7 Failed: Expected IndexError, but no error was raised"
    except IndexError:
        pass  # Expected behavior
    
    print("All test cases passed!")

def main():
    test_heap()

if __name__ == "__main__":
    main()
