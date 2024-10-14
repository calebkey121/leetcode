"""
2530. Maximal Score After Applying K Operations
Medium
Topics
Companies
Hint

You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

    choose an index i such that 0 <= i < nums.length,
    increase your score by nums[i], and
    replace nums[i] with ceil(nums[i] / 3).

Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

 

Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.

Example 2:

Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.

 

Constraints:

    1 <= nums.length, k <= 105
    1 <= nums[i] <= 109
"""
from typing import List
from math import ceil
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # we want to use a max heap to keep track of the highest value of nums
        # since heapq uses min heap we need to make our own max heap by negating the values
        maxHeap = [ -num for num in nums ]
        heapq.heapify(maxHeap)
        score = 0
        for i in range(k):
            topScore = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -ceil(topScore / 3))
            score += topScore
        return score

cases = [
    ([10,10,10,10,10], 5),
    ([1,10,3,3,3], 3),
]
answers = [
    50,
    17,
]
test_cases = [ ( a[0], a[1], b ) for a, b in zip(cases, answers) ]
sol = Solution()

for i, test_case in enumerate(test_cases):
    arr, ops, answer = test_case
    try:
        myAnswer = sol.maxKelements(arr, ops)
        assert myAnswer == answer
        print(f"Passed Test Case {i + 1}")
    except AssertionError:
        print(f"Failed Test Case {i + 1}: Got {myAnswer}, expected {answer}")
