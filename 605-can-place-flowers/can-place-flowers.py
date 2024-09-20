class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower_count = 0
        listSize = len(flowerbed)

        for i in range(listSize):
            if flowerbed[i] == 0:
                # check if left and right is empty
                is_left_empty = (i == 0) or (flowerbed[i-1] == 0)
                is_right_empty = (i == listSize - 1) or (flowerbed[i+1] == 0)

                if is_left_empty and is_right_empty:
                    # plant a flower
                    flowerbed[i] = 1
                    flower_count += 1
        
        return flower_count >= n
        
