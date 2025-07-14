from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        L = 0

        for R in range(len(nums)):

            if R - L > k:
                window.remove(nums[L])
                L += 1

            if nums[R] in window:
                return True
            else:
                window.add(nums[R])
        return False
    
duplicate = Solution()

nums1 = [1,2,3,1]
k1 = 3
nums2 = [1,0,1,1]
k2 = 1
nums3 = [1,2,3,1,2,3]
k3 = 2

sol1 = duplicate.containsNearbyDuplicate(nums1, k1)
sol2 = duplicate.containsNearbyDuplicate(nums2, k2)
sol3 = duplicate.containsNearbyDuplicate(nums3, k3)

print(f"Array: '{nums1} | K '{k1}' | Result: '{sol1}'")
print(f"Array: '{nums2} | K '{k2}' | Result: '{sol2}'")
print(f"Array: '{nums3} | K '{k3}' | Result: '{sol3}'")