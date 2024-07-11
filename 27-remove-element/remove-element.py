from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

solution = Solution()

nums1 = [3, 2, 2, 3]
val1 = 3
result1 = solution.removeElement(nums1, val1)

nums2 = [0, 1,2,2,3,0,4,2]
val2 = 2
results2 = solution.removeElement(nums2, val2)
        