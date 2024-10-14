"""
632. Smallest Range Covering Elements from K Lists
Hard
Topics
Companies

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

 

Constraints:

    nums.length == k
    1 <= k <= 3500
    1 <= nums[i].length <= 50
    -105 <= nums[i][j] <= 105
    nums[i] is sorted in non-decreasing order.

"""
from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pointers = [ 0 ] * len(nums)
        maxPointers = [ len(numList) - 1  for numList in nums ]

        # we'll use a min heap to keep track of the value at each pointer
        valueMinHeap = []
        maxPair = None
        for i, numList in enumerate(nums):
            pointer = pointers[i]
            value = numList[pointer]
            if maxPair is None:
                maxPair = (value, i)
            maxValue, maxIndex = maxPair
            if value > maxValue:
                maxPair = (value, i)
            # min heaps using tuples sort by first item, which is why the value is first
            valueMinHeap.append(( value, i ))
        heapq.heapify(valueMinHeap)
        # record the range of each interval
        minValue, minIndex = valueMinHeap[0]
        maxValue, maxIndex = maxPair
        minRangeDistance = maxValue - minValue
        minRange = [ minValue, maxValue ]
        #       *side note* if range is [1] return -> smallest possible range
        if minRangeDistance == 0: # small optimization, can't get better than a single number
            return minRange
        
        listEnded = False
        # repeat until all lists are complete (we will have some early break optimizations)
        while pointers != maxPointers:
            # increase the smallest valued pointer (will attempt to shorten range)
            popValue, popIndex = heapq.heappop(valueMinHeap)
            if pointers[popIndex] == maxPointers[popIndex]:
                listEnded = True
            else:
                pointers[popIndex] += 1
                newIndex = popIndex
                newPointer = pointers[popIndex]
                newValue = nums[newIndex][newPointer]
                if newValue > maxValue:
                    maxValue, maxIndex = newValue, newIndex
                heapq.heappush(valueMinHeap, (newValue, newIndex))
                # a list might have ended, meaning the new min heap might not be the actual min
                if listEnded:
                    minValue, minIndex = min((minValue, minIndex), valueMinHeap[0])
                else:
                    minValue, minIndex = valueMinHeap[0]
                # update minRange if needed
                newRangeDistance = maxValue - minValue
                if newRangeDistance == 0: # small optimization, cant get better than this
                    return [ minValue, maxValue ]
                elif newRangeDistance < minRangeDistance: # found smaller range
                    minRangeDistance = newRangeDistance
                    minRange = [minValue, maxValue]
                elif listEnded and newRangeDistance > minRangeDistance: # strictly increasing
                    break # since a list has already ended, we'll only ever increase, so just break
        return minRange

cases = [
    [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]],
    [[1,2,3],[1,2,3],[1,2,3]],
    [[10, 10], [11, 11]],
]
answers = [
    [ 20, 24 ],
    [ 1, 1 ],
    [ 10, 11 ],
]
test_cases = [ ( a, b ) for a, b in zip(cases, answers) ]
sol = Solution()

for i, test_case in enumerate(test_cases):
    case, answer = test_case
    try:
        myAnswer = sol.smallestRange(case)
        assert myAnswer == answer
        print(f"Passed Test Case {i + 1}")
    except AssertionError:
        print(f"Failed Test Case {i + 1}: Got {myAnswer}, expected {answer}")
