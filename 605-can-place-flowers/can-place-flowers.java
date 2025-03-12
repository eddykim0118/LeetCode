class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) {
            return true;
        }

        int length = flowerbed.length;
        int i = 0;

        while (i < length) {
            if (flowerbed[i] == 1) {
                i += 2;
                continue;
            }

            if ((i == 0 || flowerbed[i - 1] == 0) && (i == length - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                n--;
                if (n == 0) {
                    return true;
                }

                i += 2;
            } else {
                i++;
            }
        }
        return false;
    }
}