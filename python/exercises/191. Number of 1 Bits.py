class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        
        while n != 0:
            if n & 1:
                count += 1
            n >>= 1
        return count


case1 = 11
case2 = 128
case3 = 2147483645

sol = Solution()

print(f"Number: {case1} | Output: {sol.hammingWeight(case1)}")
print(f"Number: {case2} | Output: {sol.hammingWeight(case2)}")
print(f"Number: {case3} | Output: {sol.hammingWeight(case3)}")