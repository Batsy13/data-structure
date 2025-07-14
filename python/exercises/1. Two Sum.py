from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {}

        for i, number in enumerate(nums):
            diff = target - number
            if diff in previousMap:
                return [previousMap[diff], i]
            previousMap[number] = i