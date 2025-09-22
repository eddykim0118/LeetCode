class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize result with first interval
        merged = [intervals[0]]
        
        # Step 3: Process each subsequent interval
        for current in intervals[1:]:
            last_merged = merged[-1]
            
            # Check if current interval overlaps with last merged interval
            if current[0] <= last_merged[1]:
                # Overlapping: merge by extending the end time
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # Non-overlapping: add as new interval
                merged.append(current)
        
        return merged