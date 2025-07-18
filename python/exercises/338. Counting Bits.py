class Solution:
    def countBits(self, n: int) -> int:
        
        arr = []
        
        for i in range(n+1):
            counter = 0

            while i != 0:
                if (i & 1):
                    counter += 1
                i >>= 1
            arr.append(counter)
            
        return arr
                    
case1 = 2
case2 = 5

sol = Solution()

print(f"Input: {case1} | Output: {sol.countBits(case1)}")
print(f"Input: {case2} | Output: {sol.countBits(case2)}")