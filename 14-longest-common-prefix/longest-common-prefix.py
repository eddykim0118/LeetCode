from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_length = min(len(s) for s in strs)

        def is_common_prefix(length:int) -> bool:
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)
        
        low, high = 0, min_length
        while low < high:
            mid = (low + high) // 2
            if is_common_prefix(mid+1):
                low = mid + 1
            else:
                high = mid
        
        return strs[0][:low]