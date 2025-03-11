class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        length = len(flowerbed)
        i = 0

        while i < length:
            if flowerbed[i] == 1:
                i += 2
                continue
            
            if (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                n -= 1

                if n == 0:
                    return True

                i += 2
            else:
                i += 1

        return False
            