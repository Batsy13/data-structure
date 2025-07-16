class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        
        while num > 0:
            if num%2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps
    
    def numberOfSteps2(self, num: int) -> int:
        steps = 0
        
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1
                
            steps += 1
        return steps

sol = Solution()

case1 = 14  # 6
case2 = 8   # 4
case3 = 123 # 12

print(f"Number: {case1} | Steps {sol.numberOfSteps(case1)}")
print(f"Number: {case2} | Steps {sol.numberOfSteps(case2)}")
print(f"Number: {case3} | Steps {sol.numberOfSteps(case3)}\n")

# Second Function ( >> and & )

print(f"Number: {case1} | Steps {sol.numberOfSteps2(case1)}")
print(f"Number: {case2} | Steps {sol.numberOfSteps2(case2)}")
print(f"Number: {case3} | Steps {sol.numberOfSteps2(case3)}")