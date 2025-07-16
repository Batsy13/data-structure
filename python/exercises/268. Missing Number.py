from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        
        for num in nums:
            x ^= num
        for i in range(len(nums) + 1):
            x ^= i
        
        return x
    
case1 = [3,0,1]
case2 = [0,1]
case3 = [9,6,4,2,3,5,7,0,1]

sol = Solution()

print(f"Array: {case1} | Missing Number: {sol.missingNumber(case1)}")
print(f"Array: {case2} | Missing Number: {sol.missingNumber(case2)}")
print(f"Array: {case3} | Missing Number: {sol.missingNumber(case3)}")