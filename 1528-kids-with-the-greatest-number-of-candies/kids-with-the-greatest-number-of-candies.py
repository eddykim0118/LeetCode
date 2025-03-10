class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        result = []

        for candy in candies:
            if extraCandies + candy >= most:
                result.append(True)
            else:
                result.append(False)

        return result