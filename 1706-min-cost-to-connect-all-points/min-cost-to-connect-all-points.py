class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        minHeap = [(0, 0)]  # (cost, point_index)
        res = 0
        
        while len(visited) < n:
            cost, curr = heapq.heappop(minHeap)
            
            if curr in visited:
                continue
                
            res += cost
            visited.add(curr)
            
            for nxt in range(n):
                if nxt not in visited:
                    nextCost = abs(points[curr][0] - points[nxt][0]) + abs(points[curr][1] - points[nxt][1])
                    heapq.heappush(minHeap, (nextCost, nxt))
                    
        return res