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

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        return [ 20, 24 ]

cases = [
    [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]],
    [[1,2,3],[1,2,3],[1,2,3]],
]
answers = [
    [ 20, 24 ],
    [ 1, 1 ],
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
