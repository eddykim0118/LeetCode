public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) {
            return true;
        }

        int length = flowerbed.Length;
        int i = 0;

        while (i < length) {
            if (flowerbed[i] == 1) {
                i += 2;
                continue;
            }

            bool leftEmpty = (i == 0 || flowerbed[i - 1] == 0);
            bool rightEmpty = (i == length - 1 || flowerbed[i + 1] == 0);

            if (leftEmpty && rightEmpty) {
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