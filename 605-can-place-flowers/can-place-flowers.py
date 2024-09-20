class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower_count = 0
        listSize = len(flowerbed)

        for i in range(listSize):
            if flowerbed[i] == 0:
                # check if left and right is empty
                # first check if left is empty
                if i == 0:
                    is_left_empty = True
                elif flowerbed[i-1] == 0:
                    is_left_empty = True
                else:
                    is_left_empty = False

                # now check if right is empty
                if i == listSize - 1:
                    is_right_empty = True
                elif flowerbed[i+1] == 0:
                    is_right_empty = True
                else:
                    is_right_empty = False
                
                if is_left_empty and is_right_empty:
                    # plant a flower
                    flowerbed[i] = 1
                    flower_count += 1
        
        return flower_count >= n
        
