from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # in order to only have one unique element in there, I will have to use a library
        # When it comes to the library, I will have to make sure that I will pop from the list (array) any duplicates
        if not nums:
            return 0

        unique_count = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_count - 1]:
                nums[unique_count] = nums[i]
                unique_count += 1
        
        return unique_count
