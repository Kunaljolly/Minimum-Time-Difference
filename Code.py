class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(t[:2]) * 60 + int(t[3:]) for t in timePoints]
        minutes.sort()
        
        min_diff = float('inf')
        n = len(minutes)
        
        for i in range(1, n):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        
        # Handle wrap-around case
        min_diff = min(min_diff, (minutes[0] + 1440) - minutes[n-1])
        
        return min_diff
