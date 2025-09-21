class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
        
        minutes.sort()
        min_diff = float('inf')
        
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
        circular_diff = 24 * 60 - (minutes[-1] - minutes[0])
        min_diff = min(min_diff, circular_diff)
        
        return min_diff